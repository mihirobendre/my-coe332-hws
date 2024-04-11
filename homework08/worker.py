
from jobs import greturn_all_jobids, get_job_by_id, update_job_status, q, rd
import time

@q.worker
def do_work(jobid):
    update_job_status(jobid, 'in progress')
    time.sleep(30)
    update_job_status(jobid, 'complete')

do_work()



