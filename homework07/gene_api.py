
import requests
from flask import Flask, request
import redis
import json
from typing import Union, List, Dict
from jobs import add_job, get_job_by_id, rd

app = Flask(__name__)

rd: redis.Redis = redis.Redis(host='redis-db', port=6379, db=0)

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
        # Get data from web
        url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the JSON response
            full_data = response.json()
            data = full_data["response"]["docs"]
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

@app.route('/gene', methods=['GET'])
def all_genes() -> str:
    """
    Endpoint to retrieve information about all genes.

    Returns:
        str: JSON formatted list of gene IDs.
    """
    # Get data from web
    url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"
    response = requests.get(url)
    list_of_genes = []
    if response.status_code == 200:
        # Parse the JSON response
        full_data = response.json()
        data = full_data["response"]["docs"]
        for item in data:
            list_of_genes.append(item["hgnc_id"])
        return json.dumps(list_of_genes)
    else:
        print("Failed to fetch data:", response.status_code)

@app.route('/gene/<hgnc_id>', methods=['GET'])
def gene_info(hgnc_id: str) -> Union[str, None]:
    """
    Endpoint to retrieve information about a specific gene.

    Args:
        hgnc_id (str): HGNC ID of the gene.

    Returns:
        Union[str, None]: JSON formatted gene information or None if not found.
    """
    # Get data from web
    url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"
    response = requests.get(url)
    info_for_id = []
    if response.status_code == 200:
        # Parse the JSON response
        full_data = response.json()
        data = full_data["response"]["docs"]
        for item in data:
            if item["hgnc_id"] == hgnc_id:
                info_for_id = json.dumps(item)
        return info_for_id
    else:
        print("Failed to fetch data:", response.status_code)
        return None

@app.route('/jobs', methods = ['POST'])
def submit_job():
    data = request.get_json()
    job_dict = add_job(data['start'], data['end'])
    return job_dict

@app.route('/jobs/<jobid>', methods = ['GET'])
def get_job(jobid):
    return get_job_by_id(jobid)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
