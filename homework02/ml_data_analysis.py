import csv
import pprint


#function definitions:









data = {}
data['meteorite_landings'] = []

with open('Meteorite_Landings_20240206.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data['meteorite_landings'].append(dict(row))

#pprint.pprint(data)



