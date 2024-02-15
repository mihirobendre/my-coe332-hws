import csv
import pprint
import math
import numpy as np
from gcd_algorithm import calculate_great_circle_distance
import logging
import socket
import sys

#configure logging
logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

#function definitions:

def summary_stats(a_list_of_dicts: list, a_key_string: str) -> dict:
     
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
    
    logger.debug("Values after for loop: ")
    logger.debug("Total: " + str(total))
    logger.debug("List of all: " + str(list_of_all_values))
    length = len(list_of_all_values)

    # if length is even
    if length % 2 == 0:
        # then calculate median as average of 2 middle values
        median_val = (list_of_all_values[math.floor(float(length)/2-1)] + list_of_all_values[math.floor(float(length) / 2)]) / 2.0

    else:
        # calculate median as just middle value
        median_val = list_of_all_values[math.floor(length / 2)]
 
    # calculation of mean
    mean_val = (total / len(a_list_of_dicts))

    # Logging mean and median
    logger.debug("Mean: %s" % mean_val)
    logger.debug("Median: %s" % median_val)

    result = {"Mean":mean_val, "Median":median_val}
    
    return result

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
        if current_dict[a_key_string] == None:
            converted = False
        else:
            try:
                float_val = float(a_list_of_dicts[i][a_key_string])
            except ValueError:
                logger.info("Index %s of input dict, string not convertable to float" %i)
                converted = False
        if converted == True:
            new_list_of_dicts.append(current_dict)
        
    return new_list_of_dicts

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
    # retreiving coordinates from list of dicts
    lat1 = float(a_list_of_dicts[point_1_index][lat_key_string])
    long1 = float(a_list_of_dicts[point_1_index][long_key_string])
    lat2 = float(a_list_of_dicts[point_2_index][lat_key_string])
    long2 = float(a_list_of_dicts[point_2_index][long_key_string])
    logger.debug("Coordinates retreived from provided list of dicts: ")
    logger.debug("lat1: " + str(lat1))
    logger.debug("long1: " + str(long1))
    logger.debug("lat2: " + str(lat2))
    logger.debug("long2: " + str(long2))

    return calculate_great_circle_distance(lat1, long1, lat2, long2)

def main():
	
    data = {}
    data['meteorite_landings'] = []
	
    with open('Meteorite_Landings_20240206.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['meteorite_landings'].append(dict(row))
    	
    cleaned_data = remove_nulls(data['meteorite_landings'], 'mass (g)')
    
    #ori_len = len(data['meteorite_landings'])
    #new_len = len(cleaned_data)

    #pprint.pprint(cleaned_data)
   
    print(summary_stats(cleaned_data, 'mass (g)'))

	
#    print("Original length: ", ori_len)
#    print("New length: ", new_len)
	
#    print("Diff: ", ori_len - new_len)
	
    distance = calculate_distance(data['meteorite_landings'], 'reclat', 'reclong', 0, 1)

    print("Distance between first two points:", distance)



if __name__ == '__main__':
    main()

#pprint.pprint(data)


