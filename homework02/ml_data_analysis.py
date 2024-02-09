import csv
import pprint
import math
import numpy as np
import gcd_algorithm
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



#function definitions:

def summary_stats(a_list_of_dicts, a_key_string):
     total = 0.0
     median_list = []
 
     for i in range(len(a_list_of_dicts)):
         total += float(a_list_of_dicts[i][a_key_string])
         median_list.append(float(a_list_of_dicts[i][a_key_string]))
 
     length = len(median_list)
     if length % 2 == 0:
         median_val = (median_list[length // 2 - 1] + median_list[length // 2]) / 2.0
     else:
         median_val = median_list[math.floor(length / 2)]
 
     mean_val = (total / len(a_list_of_dicts))
     print("Mean:", mean_val)
     print("Median:", median_val)

def remove_nulls(a_list_of_dicts, a_key_string):
	new_list_of_dicts = []
	for i in range(len(a_list_of_dicts)):
		current_dict = a_list_of_dicts[i]
		converted = True
		try:
			float_val = float(a_list_of_dicts[i][a_key_string])
		except ValueError:
			converted = False

		if converted == True:
			new_list_of_dicts.append(current_dict)
	
	return new_list_of_dicts
	#pprint.pprint(new_list_of_dicts)

#Distance Calculation Algorithm

def calculate_distance_between_sites(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """

    This function calculates the great-circle distance between two geographical coordinates.

    Arguments:
        lat1: Latitude of the first location.
        lon1: Longitude of the first location.
        lat2: Latitude of the second location.
        lon2: Longitude of the second location.

    Returns:
        Great-circle distance between the two locations in kilometers.
    """
    return calculate_great_circle_distance(lat1, lon1, lat2, lon2)

def main():

	data = {}
	data['meteorite_landings'] = []


	with open('Meteorite_Landings_20240206.csv', 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			data['meteorite_landings'].append(dict(row))



	cleaned_data = remove_nulls(data['meteorite_landings'], 'mass (g)')

	ori_len = len(data['meteorite_landings'])
	new_len = len(cleaned_data)

	summary_stats(cleaned_data, 'mass (g)')

	print("Original length: ", ori_len)
	print("New length: ", new_len)

	print("Diff: ", ori_len - new_len)

	print("Distance between first two points:")

if __name__ == '__main__':
    main()

#pprint.pprint(data)



