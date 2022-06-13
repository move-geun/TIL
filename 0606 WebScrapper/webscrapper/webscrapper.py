from indeed import indeed_get_job
from stackover import stackover_get_job
from save import indeed_save_file, stackover_save_file

indeed_jobs = indeed_get_job()
stackover_companys = stackover_get_job()
indeed_save_file(indeed_jobs)
stackover_save_file(stackover_companys)
