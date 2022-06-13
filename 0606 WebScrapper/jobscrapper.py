import requests
from bs4 import BeautifulSoup

LIMIT = 50

def indeed_last_pn(url):
    indeed_result = requests.get(url)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    page_ul = indeed_soup.find("ul", {"class":"pagination-list"})
    page_lis = page_ul.find_all("li")

    span_list = list()

    for page_li in page_lis[:-1]:
        span = page_li.find("span",{"class":"pn"})
        if span:
            span_list.append(int(span.string))


    max_pn = span_list[-1]
    return max_pn



def job_info(info):
    title = info.find("a").find("span").string
    company = info.find("span", {"class":"companyName"}).string
    location = info.find("div", {"class":"companyLocation"}).string
    job_id = info.find("a")["data-jk"]
    link = f'https://kr.indeed.com/채용보기?jk={job_id}'
    return {
        "title" : title,
        "company" : company,
        "location" : location,
        "link" : link,
    }



def indeed_page_change(num, url):
    view_jobs = list()
    for n in range(num):
        result = requests.get(f'{url}&start={LIMIT*n}')
        indeed_soup = BeautifulSoup(result.text, "html.parser")
        result_contents = indeed_soup.find_all("td",{"class":"resultContent"})
        for result_content in result_contents:
            view_job = job_info(result_content)
            view_jobs.append(view_job)
    return view_jobs


def indeed_get_job(word):
    url = f"https://kr.indeed.com/jobs?q={word}&limit={LIMIT}"
    last_num = indeed_last_pn(url)
    return indeed_page_change(last_num, url)