import pyspectroworks
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import re

api_key = "ZWZhMWQ1MTQtOGM4MS00YzI1LWJiY2UtNTg3YWY1MGI5ZmQ0"

conn = pyspectroworks.connect(api_key)  # change this to match your API key

# list projects
print('PROJECTS: ')
print('{: >3} {: >24} {: >24}'.format(' ', 'NAME', 'CREATED'))
projects = conn.get_projects()
for i, project in enumerate(projects):
    timestamp = datetime.utcfromtimestamp(project.created/1000).strftime('%Y-%m-%d %H:%M:%S')
    print('{: >3} {: >24} {: >24} '.format(i, project.project_name, timestamp))

project = projects[0]
print('\n\nOPENING PROJECT "{}":'.format(project.project_name))
# load all files in project
print('{: >6}{: >2}\t{: >8}'.format('CUVETTE', ' ', 'REFRACTIVE INDEX'))
items = project.get_items()
for item in items:
    res = item.results.get('refractive_index', {})
    ri = res.get('value', 'N/A')
    print('{: >6}{:0>2}\t{: >8}'.format(item.box_code, item.cuvette_idx, ri))

sample_name = item.sample_attributes['Sample name']

## Plotting
# Simple plotting
plt.figure()

for item in items:
    sample_name = item.sample_attributes['Sample name']
    sample_spectrum = np.array(item.get_spectrum('sample_A'))
    plt.plot(sample_spectrum[:, 0], sample_spectrum[:, 1], label=sample_name)

plt.xlim([200,800])
plt.ylim(0.0, 4.0)
plt.legend()
plt.xlabel('Wavelength [nm]')
plt.ylabel('Attenuance')
plt.show()

# get spectrum of a particular item
# print('\n\nLOADING SPECTRUM: ')
item = items[0]
spectrum = item.get_spectrum('sample_B')
# print(spectrum)