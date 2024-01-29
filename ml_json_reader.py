import json
import pprint
import numpy as np

def summary_stats(a_list_of_dicts, a_key_string):
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
mean_mass = (total_mass / len(a_list_of_dicts))
print("Mean: " + mean_mass)


with open('Meteorite_Landings.json', 'r') as f:
    ml_data = json.load(f)

#pprint.pprint(ml_data)


