import csv
import pprint
import math
import numpy as np
from gcd_algorithm import calculate_great_circle_distance
import logging

#configure logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

#function definitions:

def summary_stats(a_list_of_dicts: list, a_key_string: str):
     
    """
    Calculates the mean and median of numerical values corresponding to a specified key
    within a list of dictionaries.
    
    Args:
        a_list_of_dicts (list): A list of dictionaries where each dictionary represents
            a data record.
        a_key_string (str): The key string corresponding to the numerical values for
            which mean and median are to be calculated.

    Returns:
        None. Prints the mean and median values calculated from the numerical values
        corresponding to the specified key within the list of dictionaries.
    """
    
    total = 0.0
    list_of_all_values = []
	
    for i in range(len(a_list_of_dicts)):
        total += float(a_list_of_dicts[i][a_key_string])
        list_of_all_values.append(float(a_list_of_dicts[i][a_key_string]))

    #print(list_of_all_values)
    length = len(list_of_all_values)

    if length % 2 == 0:
    	median_val = (list_of_all_values[math.floor(length/2)] + list_of_all_values[math.floor(length / 2)]) / 2.0
    else:
    	median_val = list_of_all_values[math.floor(length / 2)]
 
    mean_val = (total / len(a_list_of_dicts))
    print("Mean:", mean_val)
    print("Median:", median_val)


def remove_nulls(a_list_of_dicts: list, a_key_string: str) -> list:
	
    """
    Removes dictionaries from a list where the value corresponding to the specified key 
    cannot be converted to a float.
	
    Args:
        a_list_of_dicts (list): A list of dictionaries where each dictionary represents 
            a data record.
        a_key_string (str): The key string corresponding to the values to be checked 
            for conversion to float.
	
    Returns:
        list: A new list of dictionaries containing only those dictionaries from the 
        input list where the value corresponding to the specified key can be converted 
        to a float.
	"""
	
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

def calculate_distance(a_list_of_dicts: list, lat_key_string: str, long_key_string: str, point_1_index: int, point_2_index: int) -> float:

    """
    Calculates the great-circle distance between two geographical coordinates 
    using the Haversine formula.

    Args:
        a_list_of_dicts (list): A list of dictionaries where each dictionary 
            represents a data record.
        lat_key_string (str): The key string corresponding to the latitude values 
            in the dictionaries.
        long_key_string (str): The key string corresponding to the longitude values 
            in the dictionaries.
        point_1_index (int): The index of the first geographical coordinate in 
            the list of dictionaries.
        point_2_index (int): The index of the second geographical coordinate in 
            the list of dictionaries.

    Returns:
        float: The great-circle distance between the two geographical coordinates 
        in kilometers.
    """

    lat1 = float(a_list_of_dicts[point_1_index][lat_key_string])
    #print(lat1)
    long1 = float(a_list_of_dicts[point_1_index][long_key_string])
    lat2 = float(a_list_of_dicts[point_2_index][lat_key_string])
    long2 = float(a_list_of_dicts[point_2_index][long_key_string])
    return calculate_great_circle_distance(lat1, long1, lat2, long2)

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

    #pprint.pprint(cleaned_data)
    
    #summary_stats(cleaned_data, 'mass (g)')
	
    print("Original length: ", ori_len)
    print("New length: ", new_len)
	
    print("Diff: ", ori_len - new_len)
	
    distance = calculate_distance(data['meteorite_landings'], 'reclat', 'reclong', 0, 1)

    print("Distance between first two points:", distance)


if __name__ == '__main__':
    main()

#pprint.pprint(data)



