from indeed import indeed_get_job
from stackover import stackover_get_job

indeed_jobs = indeed_get_job()
stackover_jobs = stackover_get_job()
jobs = indeed_jobs + stackover_jobs
print(jobs)