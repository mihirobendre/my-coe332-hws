
import requests
from flask import Flask, request, jsonify
import redis
import json
from typing import Union, List, Dict
from jobs import add_job, get_job_by_id, rd, return_all_jobids

app = Flask(__name__)

_redis_ip = os.environ.get('REDIS_IP')

rd = redis.Redis(host=_redis_ip, port=6379, db=0)
res = redis.Redis(host=_redis_ip, port = 6379, db = 3)

url = "https://data.austintexas.gov/resource/fdj4-gpfu.json"

@app.route('/', methods=['GET'])
def hello_world() -> str:
    """
    Root endpoint returning a simple greeting message.

    Returns:
        str: Greeting message.
    """
    return 'Hello, world!\n'

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def handle_data() -> Union[str, List[Dict[str, str]]]:
    """
    Endpoint to handle data operations (GET, POST, DELETE).

    Returns:
        Union[str, List[Dict[str, str]]]: Response message or data.
    """
    if request.method == 'POST':
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            my_id = 0
            for item in data:
                rd.set(str(my_id), json.dumps(item))
                my_id += 1
            return 'Data loaded\n'
        else:
            print("Failed to fetch data:", response.status_code)
    elif request.method == 'GET':
        return_value = []
        for item in rd.keys():
            return_value.append(json.loads(rd.get(item)))
        return return_value
    elif request.method == 'DELETE':
        # Delete everything in redis
        for item in rd.keys():
            rd.delete(item)
        return 'Data deleted\n'
    else:
        return 'Not possible\n'

@app.route('/crimes', methods=['GET'])
def all_crimes() -> str:
    """
    Endpoint to retrieve information about all crimes.

    Returns:
        str: JSON formatted list of crime IDs.
    """
    # Get data from web
    response = requests.get(url)
    list_of_crimes = []
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        for item in data:
            list_of_crimes.append(item["incident_report_number"])
        return json.dumps(list_of_crimes)
    else:
        print("Failed to fetch data:", response.status_code)

@app.route('/crimes/<ir_num>', methods=['GET'])
def crime_info(ir_num: str) -> Union[str, None]:
    """
    Endpoint to retrieve information about a specific crime.

    Args:
        incident_report_number (str): ID of the crime.

    Returns:
        Union[str, None]: JSON formatted crime information or None if not found.
    """
    # Get data from web
    response = requests.get(url)
    info_for_id = []
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        for item in data:
            if item["incident_report_number"] == ir_num:
                info_for_id = json.dumps(item)
            return info_for_id

    else:
        print("Failed to fetch data:", response.status_code)
        return None

@app.route('/jobs', methods = ['GET','POST'])
def jobs_general():
    if request.method == 'POST':
        data = request.get_json()
        crime_type = None
        # add more parameters here        
        try:
            crime_type = data['crime_type']
            # add more parameters here
        except KeyError:
            return "The data doesn't contain the parameter(s) you requested'\n"
        
        job_dict = add_job(crime_type)
        return job_dict
    elif request.method == 'GET':
        ret_string = return_all_jobids() + '\n'
        return ret_string

@app.route('/jobs/<jobid>', methods = ['GET'])
def get_job(jobid):
    return json.loads(get_job_by_id(jobid))


@app.route('/results/<jobid>', methods = ['GET'])
def calculate_result(jobid):
    # return computed outcome for that jobid

    #get crime_type for respective jobid
    crime_type = json.loads(get_job_by_id(jobid))["crime_type"]

    result = res.get("result") 

'''
    #load dataset
    response = requests.get(url)
    info_for_id = []
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        for item in data:
            if item["crime_type"] == crime_type:
                info_for_id = json.dumps(item)
    else:
        print("Failed to fetch data:", response.status_code)
'''
    return result

    # computation/work happens in worker

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
