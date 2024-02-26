
import requests
import xmltodict
import pprint
import logging
from datetime import datetime
import math

#configure logging
logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

def speed_calculator(x_vel, y_vel, z_vel):
    
    '''
    Calculate the magnitude of velocity (speed) given its components in three dimensions.

    Parameters:
    x_vel (float): The velocity component along the x-axis.
    y_vel (float): The velocity component along the y-axis.
    z_vel (float): The velocity component along the z-axis.

    Returns:
    float: The magnitude of velocity (speed) calculated using the Euclidean distance formula.
    '''

    speed = math.sqrt(x_vel**2 + y_vel**2 + z_vel**2)
    return speed

def main():
    
    #fetching and parsing the data

    response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')

    status_code = response.status_code
    
    if status_code == 200:
        logger.info("Successfully fetched data")
    else:
        logger.error("Failed to fetch data")

    full_data_xml = response.content
    
    full_data_dicts = xmltodict.parse(full_data_xml)
    
    if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
        pprint.pprint(full_data_dicts)

    # now, printing statement about the range of data from 1st and last epochs
    stateVector = full_data_dicts['ndm']['oem']['body']['segment']['data']['stateVector']
    
    # pprint.pprint(stateVector)

    length_of_stateVector = len(stateVector)
    print("Length of stateVector: ", length_of_stateVector)
    first_epoch = stateVector[0]['EPOCH']
    print("First epoch: ", first_epoch)
    last_epoch = stateVector[length_of_stateVector - 1]['EPOCH']
    print("Last epoch: ", last_epoch)
    
    first_epoch_day_number = int(first_epoch[5:8])
    last_epoch_day_number = int(last_epoch[5:8])

    # figure out how wide this range is (how many days), and the dates it spans
    range_of_stateVector = last_epoch_day_number - first_epoch_day_number

    print("Range of stateVector (days): ", range_of_stateVector)
    
    # then, print full epoch closest to now
    current_date = datetime.now().date()
    print("Current date: ", current_date)
   
    # Specific date
    year_first_day = datetime(datetime.now().year, 1, 1)

    # Current date
    current_date_and_time = datetime.now()
    print("Current date and time: ", current_date_and_time)
    current_hour = int(str(current_date_and_time)[11:13])
    current_min = int(str(current_date_and_time)[14:16])

    print("Current hour: ", current_hour)
    print("Current minute: ", current_min)

    # printing statement about range of data, using timestamps from first and last epochs
    # Calculate the difference in days
    days_since_start_of_year = int((current_date_and_time - year_first_day).days)

    print("Number of days since start of year:", days_since_start_of_year)
    current_day = days_since_start_of_year

    list_of_minutes = []

    for instance in stateVector:
        epoch_string = instance['EPOCH']
        day_number = int(epoch_string[5:8])
        hour = int(epoch_string[9:11])
        minute = int(epoch_string[12:14])
        
        if day_number == current_day:
            if hour == current_hour:
                list_of_minutes.append({'minute_val':minute, 'index':stateVector.index(instance)})

    print("List of minute values within the current hour: ")
    pprint.pprint(list_of_minutes)

    closest_value = None
    closest_value_index = None
    min_difference = float('inf')

    for value in list_of_minutes:
        min_in_list = value['minute_val']
        index_of_min_in_list = value['index']

        difference = abs(min_in_list - current_min)    
        if difference < min_difference:
            min_difference = difference
            closest_value = min_in_list
            closest_value_index = index_of_min_in_list

    print("Closest value: ", closest_value)

    print("Closest value's index: ", closest_value_index)

    #instantaneous speed:
    
    x_dot_inst = float(stateVector[closest_value_index]['X_DOT']['#text'])
    y_dot_inst = float(stateVector[closest_value_index]['Y_DOT']['#text'])
    z_dot_inst = float(stateVector[closest_value_index]['Z_DOT']['#text'])

    speed_inst = speed_calculator(x_dot_inst, y_dot_inst, z_dot_inst)
    print("Instantaneous speed: ", speed_inst)
    
    #average speed:

    print("Epoch of the closest value to current time: ", stateVector[closest_value_index]['EPOCH'])

    speed_vector = []

    for value in stateVector:
        x_dot = float(value['X_DOT']['#text'])
        y_dot = float(value['Y_DOT']['#text'])
        z_dot = float(value['Z_DOT']['#text'])
        speed = speed_calculator(x_dot, y_dot, z_dot)
        speed_vector.append(speed)
    

    # pprint.pprint(speed_vector)
    
    average_speed = sum(speed_vector) / len(speed_vector)

    print("Average speed of ISS: ", average_speed)

if __name__ == "__main__":
    main()



