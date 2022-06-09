import csv

def indeed_save_file(jobs):
    file = open('indeed_jobs.csv', mode='w', encoding = "utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return 

def stackover_save_file(jobs):
    file = open('stackover_jobs.csv', mode='w', encoding = "utf-8")
    writer = csv.writer(file)
    writer.writerow(["company", "region", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return 