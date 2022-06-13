import requests
from bs4 import BeautifulSoup

# 주소 가져오기
LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

# 오류 없는지 확인
# print(URL)    # <Response [200]>
# print(URL.text)

# bs4가 공식문서 참고(사용법)
def indeed_last_pn():  # 페이지만 뽑아오기 // pagenation의 마지막 숫자 뽑기
    indeed_result = requests.get(URL)
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    page_ul = indeed_soup.find("ul", {"class":"pagination-list"})
    page_lis = page_ul.find_all("li")

    span_list = list()

    for page_li in page_lis[:-1]:
        span = page_li.find("span",{"class":"pn"})
        if span:
            span_list.append(int(span.string))

    # 현재 pagenation의 가장 큰 숫자
    max_pn = span_list[-1]
    return max_pn


# job 정보들 받아오기
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


# page 변경하면서 job 받아오기
def indeed_page_change(num):
    view_jobs = list()
    for n in range(num):
        result = requests.get(f'{URL}&start={LIMIT*n}')
        indeed_soup = BeautifulSoup(result.text, "html.parser")
        result_contents = indeed_soup.find_all("td",{"class":"resultContent"})
        for result_content in result_contents:
            view_job = job_info(result_content)
            view_jobs.append(view_job)
    return view_jobs


def indeed_get_job():
    last_num = indeed_last_pn()
    return indeed_page_change(last_num)