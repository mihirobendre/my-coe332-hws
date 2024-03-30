import requests
import pprint
from flask import Flask, request
import redis
import json


app = Flask(__name__)

rd = redis.Redis(host = 'redis-db', port = 6379, db = 0)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!\n'

@app.route('/data', methods=['GET','POST','DELETE'])
def handle_data():
    if request.method == 'POST':
        # get data from web
        url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the JSON response
            full_data = response.json()
            data = full_data["response"]["docs"]
            my_id = 0
            for item in data:
                
                rd.set(my_id,json.dumps(item) )
                my_id += 1
            return 'Data loaded\n'
        else:
            print("Failed to fetch data:", response.status_code)

    elif request.method == 'GET':
        
        return_value = []
        for item in rd.keys():
            return_value.append(json.loads(rd.get(item)))
        return return_value

        # iterate over keys in redis
        # return everything as a json object

    elif request.method == 'DELETE':
        # delete everything in redis
        for item in rd.keys():
            rd.delete(item)
        return 'Data deleted\n'
    else:
        return 'Not possible\n'

@app.route('/gene',methods = ['GET'])
def all_genes():
    # get data from web
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

@app.route('/gene/<hgnc_id>',methods = ['GET'])
def gene_info(hgnc_id):
    # get data from web
    url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"
    response = requests.get(url)
    info_for_id = []
    if response.status_code == 200:
        # Parse the JSON response
        full_data = response.json()
        data = full_data["response"]["docs"]
        for item in data:
            #list_of_genes.append(item["hgnc_id"])
            if item["hgnc_id"] == hgnc_id:
                info_for_id = json.dumps(item)
        return info_for_id
    else:
        print("Failed to fetch data:", response.status_code)
        return None

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
