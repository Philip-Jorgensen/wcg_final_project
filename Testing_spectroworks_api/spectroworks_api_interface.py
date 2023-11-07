"""
This code is a rewrite of the "pyspectroworks.py" file
It is tailoring it to our needs.

- Philip J
"""
# Imports
import json
import requests
from datetime import datetime
from typing import Dict, List, Tuple
import re
from math import sqrt

# Constants
API_KEY = "ZWZhMWQ1MTQtOGM4MS00YzI1LWJiY2UtNTg3YWY1MGI5ZmQ0"

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
    

    def get_project(self, project_name: str = None) -> list:
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

def analyze_test(project: Project, test_number: int, moving_average: bool = False):
    refractive_index = []    
    time = []

    for i, item in enumerate(project.items):
        if item.test_number == test_number and not item.water_reference:
            refractive_index.append((item.results.get('refractive_index', {})).get('value', 'N/A'))
            time.append(item.measurement_time)

    if moving_average:
        window_size = 3

        ri_moving_average = []
        i = 0
        while i < len(refractive_index) - window_size + 1:
            window = refractive_index[i : i + window_size]
            window_average = sum(window) / window_size

            ri_moving_average.append(window_average)

            i += 1
        
        return ri_moving_average

    return refractive_index
    

def main():
    connection = Connection(API_KEY, f'https://api.spectroworks.com/prod/api/')

    project = connection.get_project('Vinyl chloride in water')
    project.get_items()

    refractive_index = analyze_test(project, 11, True)

    ri_shift = max(refractive_index) - refractive_index[0]

    print(ri_shift)


# Only allow the program to be run directly, not as an import
if __name__ == '__main__':
    main()

