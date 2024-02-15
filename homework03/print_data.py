import pprint
import csv

data = {}
data['meteorite_landings'] = []


with open('Meteorite_Landings_20240206.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data['meteorite_landings'].append(dict(row))

short_data = []
for i in range(0,5):
	short_data.append(data['meteorite_landings'][i])

pprint.pprint(short_data)

