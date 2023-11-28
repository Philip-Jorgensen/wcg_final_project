"""
This code is a rewrite of the "pyspectroworks.py" file
It is tailoring it to our needs.

- Philip J
"""
# Imports
import json
import requests
from typing import Dict
import re
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

from dataclasses import dataclass

# Constants
API_KEY = "ZWZhMWQ1MTQtOGM4MS00YzI1LWJiY2UtNTg3YWY1MGI5ZmQ0"
ALL_PROJECTS_KEY = "ODE2NmRhZTctM2IwMC00YzAwLTllYzgtOWIyM2E3NjczYjU4"

# Classes
class Connection:
    def __init__(self, api_key: str, url: str):
        """
        Initializes Connection object.
        :param api_key: str, API key for the connection.
        :param url: str, URL of the connection.
        """
        self.api_key = api_key
        self.url = url
        self.projects = None
    

    def get_project(self, project_name: str = None):
        """
        Returns a list of projects.
        :return: list of Project objects.
        """
        # load projects
        if self.projects is None: # If you haven't loaded the projects earlier
            res = requests.get(self.url + 'list_projects', params={'api_key': self.api_key}) # response
            if res.status_code != 200: # Response is not OK (200)
                raise ConnectionError(json.loads(res.text)['message'])
            projects = json.loads(res.text)['message']['items']
            for i, project in enumerate(projects):
                if project['project_name'] == project_name:
                    return Project(self, projects[i])

class Project:
    def __init__(self, connection: Connection, data: dict):

        self.connection = connection

        self._project_id = data['project_id']
        self.project_name = data.get('project_name', '')
        self.num_files = int(data.get('num_files', 0))
        self.created = float(data.get('created', 0)) / 1000
        self.modified = float(data.get('modified', 0)) / 1000
        self.results = data.get('results', [])
        self.items = None
    
    def get_items(self) -> list:

        if self.items is None:
            res = requests.get(self.connection.url + 'list_files_by_project',
                                params={'api_key': self.connection.api_key,
                                        'project_id': int(self._project_id),
                                        'max_files': 1000})
            data = json.loads(res.text)['message']
            if res.status_code != 200:
                raise ConnectionError(data)
            file_list = data['items']

            # IDs for the different files in the project
            file_ids = [file['file_id'] for file in file_list]
            res = requests.post(self.connection.url + 'get_files',
                                params={'api_key': self.connection.api_key},
                                data=json.dumps(file_ids))

            data = json.loads(res.text)['message']
            if res.status_code != 200:
                raise ConnectionError(data)

            sort_by_created = lambda item : item.created
            
            items = data['items']
            
            items = [Item(self.connection, item, self) for item in items]
            self.items = [item for item in items if item.completeness == 100 and not item.hidden]
            self.items.sort(key=sort_by_created)

            return self.items

class Item:
    def __init__(self, connection: Connection, data: Dict = None, project: Project = None):

        self.connection = connection
        if data is None:
            data = {}
        self._file_id = data['file_id']
        self._project_id = data['project_id']
        self.project = project
        self.created = float(data.get('created', 0)) / 1000
        self.modified = float(data.get('modified', 0)) / 1000
        self.cuvette_idx = int(data.get('cuvette_idx', -1))
        self.box_code = data.get('box_code', None)
        self.completeness = int(data.get('completeness', 0))
        self.hidden = bool(data.get('file_hidden', False))
        self.results = data.get('results', {})
        self.user_note = data.get('user_note', '')
        self.reference_name = data.get('ref_name', '')
        self.reference_ri = self.c1_to_n(data.get('ref_c1', 0.0))

        self.sample_attributes = {}
        sample_attributes = data.get('input_tags', {})
        for key, val in sample_attributes.items():
            self.sample_attributes[key] = val['value']

        # Custom properties, properties that is inside the sample name
        try:
            self.sample_name = self.sample_attributes['Sample name']
        except KeyError:
            self.sample_name = "N/A"

        ## Test number
        test_number = re.findall(r'T\d+', self.sample_name)
        self.test_number = int(test_number[0][1:]) if test_number else None

        ## measurement number
        measurement_time = re.findall(r'\d+\.?\d*min', self.sample_name)
        self.measurement_time = float(measurement_time[0][:-3]) if measurement_time else None

        ## Water reference
        self.water_reference = (len(re.findall(r'water reference', self.sample_name.lower()))) != 0

    @staticmethod
    def c1_to_n(c1):
        n_water = 1.3332153809611258
        pmt_water = n_water ** 2
        pmt = 1 + (pmt_water - 1) * c1
        return sqrt(pmt)

@dataclass
class Data:
    time: list
    refractive_index: list
    ri_shift: float
    test_number: int
    moving_average: bool = False
    moving_average_data: tuple = ()
    outliers_removed: bool = False
    vc_concentration: float = 0

ri_shift_formula = lambda ri : max(ri) - ri[0]

def analyze_test(project: Project, test_number: int, moving_average: bool = False, remove_outliers: bool = False) -> Data:
    refractive_index = []
    time = []


    for i, item in enumerate(project.items):
        if item.test_number == test_number and not item.water_reference:
            refractive_index.append((item.results.get('refractive_index', {})).get('value', 'N/A'))
            time.append(item.measurement_time)
            solvent = item.sample_attributes['Solvent']
            analyte = item.sample_attributes['Analyte']

    di_volume = float(re.findall(r'\d+\.*\d*ml',solvent)[0][:-2]) # ml
    vc_volume = float(re.findall(r'\d+\.*\d*ul', analyte)[0][:-2]) # ul
    
    if moving_average:
        window_size = 3

        ri_moving_average = []
        i = 0
        while i < len(refractive_index) - window_size + 1:
            window = refractive_index[i : i + window_size]
            window_average = sum(window) / window_size

            ri_moving_average.append(window_average)

            i += 1

        result = Data(
            time = time,
            refractive_index= refractive_index,
            ri_shift=ri_shift_formula(ri_moving_average),
            moving_average = True,
            moving_average_data=(time[1:-1], ri_moving_average),
            test_number = test_number
        ) 
    else:
        result = Data(time, refractive_index, ri_shift_formula(refractive_index), test_number=test_number)

    if remove_outliers:
        std = 2*np.std(result.refractive_index)
        mean = np.mean(result.refractive_index)

        result.outliers_removed = True

        ri_no_outliers = []
        time_no_outliers = []

        for i, item in enumerate(result.refractive_index):
            if item < mean + std or item > mean - std:
                ri_no_outliers.append(item)
                time_no_outliers.append(result.time[i])
        
        result.refractive_index = ri_no_outliers

    result.vc_concentration = (float(vc_volume)*2)/float(di_volume)
    return result

def analyze_range(tests_list: list, project: Project, moving_average: bool, remove_outliers: bool) -> list:
    ri_shift_list = []
    vc_concentration_list = []

    for i in tests_list:
        item_data = analyze_test(project, i, moving_average, remove_outliers)
        ri_shift_list.append(item_data.ri_shift)
        vc_concentration_list.append(item_data.vc_concentration)

    return (vc_concentration_list, ri_shift_list)

def plotting(data: Data):
    time = data.time
    values = data.refractive_index

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    axis.plot(time, values, label=f"Measurement {'- Outliers removed' if data.outliers_removed else ''}")
    if data.moving_average:
        axis.plot(data.moving_average_data[0], data.moving_average_data[1], label="Moving average")
    axis.grid(True)

    axis.set_title(f"Refractive index graph, T{data.test_number} {'- Moving average ' if data.moving_average else '' }{'- Outliers removed' if data.outliers_removed else ''}")
    axis.set_xlim(min(time), max(time))
    axis.set_xlabel("Minutes")
    axis.set_ylabel("Refractive index")
    axis.legend()

    return (axis, fig)
    
def ri_shift_plot(ri_shift_data: tuple):
    plt.plot(ri_shift_data[0], ri_shift_data[1])
    plt.grid(True)

    plt.xlabel("VC Concentration (ug/ml)")
    plt.ylabel("RI Shift")

    plt.show()

def main():
    connection = Connection(API_KEY, f'https://api.spectroworks.com/prod/api/')

    project = connection.get_project('Vinyl chloride in water')
    project.get_items()

    # refractive_index = analyze_test(
    #     project, 
    #     test_number = 13,
    #     moving_average = True,
    #     remove_outliers = True
    #     )
    
    ri_shift_data = analyze_range([9, 10], project, True, True)
    ri_shift_plot(ri_shift_data)


# Only allow the program to be run directly, not as an import
if __name__ == '__main__':
    main()