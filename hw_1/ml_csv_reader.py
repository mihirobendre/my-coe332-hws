import json
import pprint
import numpy as np
import math
import csv

def summary_stats(a_list_of_dicts, a_key_string):
    total_mass = 0.0
    median_list = []

    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
        median_list.append(float(a_list_of_dicts[i][a_key_string]))
        
    length = len(median_list)
    if length % 2 == 0:
        median_val = (median_list[length // 2 - 1] + median_list[length // 2]) / 2.0
    else:
        median_val = median_list[math.floor(length / 2)]

    mean_mass = (total_mass / len(a_list_of_dicts))
    print("Mean:", mean_mass)
    print("Median:", median_val)

data = {}
data['meteorite_landings'] = []

with open('Meteorite_Landings.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data['meteorite_landings'].append(dict(row))

#pprint.pprint(data)

summary_stats(data['meteorite_landings'], 'mass (g)')







