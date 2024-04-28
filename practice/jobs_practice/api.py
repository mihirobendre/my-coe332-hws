
from flask import Flask, request
from jobs import add_job, get_job_by_id, rd

app = Flask(__name__)

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


