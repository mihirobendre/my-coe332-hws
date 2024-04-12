import json
from jobs import return_all_jobids, get_job_by_id, update_job_status, q, rd, jdb
import time

_redis_ip = os.environ.get('REDIS_IP')
_redis_port = '6379'
_list_of_jobs = []

rd = redis.Redis(host=_redis_ip, port=6379, db=0)
q = HotQueue("queue", host=_redis_ip, port=6379, db=1)
jdb = redis.Redis(host=_redis_ip, port=6379, db=2)
res = redis.Redis(host=_redis_ip, port=6379, db = 3)

'''
@q.worker
def map_by_crime_type(jobid):
    update_job_status(jobid, 'in progress')
    # get crime_type paramter from jobs database
    crime_type = json.loads(get_job_by_id(jobid))["crime_type"]
    
    # create filtered list of dicts from raw data, containing only dicts of desired category
    filtered_data = []
    for item in rd.keys():
        if item["crime_type"] == crime_type:
            filtered_data.append(json.loads(rd.get(item)))
    
    # save sample result: filtered data
    res.set("result", json.dumps(filtered_data))

    # produce geospatial map of these crimes around Austin, TX
    
    
    # upload an image of this map to by res database
    
    
    update_job_status(jobid, 'complete')

map_by_crime_type()
'''

@q.worker
def do_work():
    update_job_status(jobid, 'in progress')
    update_job_status(jobid, 'complete')

do_work()


