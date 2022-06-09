import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs/companies?q=python"

def stackover_last_pn():
    nums = list()
    stackover_result = requests.get(URL)
    stackover_soup = BeautifulSoup(stackover_result.text, "html.parser")
    paginations = stackover_soup.find_all("a", {"class":"s-pagination--item"})
    for pagination in paginations:
        nums.append(pagination.find("span").string)
    nums = nums[:-1]
    return int(max(nums))


def company_info(html):
    title = html.find("a",{"class":"s-link"}).string
    region_rows = html.find_all("div",{"class":"fs-body1"})
    region = region_rows[1].get_text()
    location = region_rows[2].get_text()
    ex_link = html.find("a",{"class":"s-link"})["href"]
    link = f'https://stackoverflow.com/{ex_link}'
    return {
        "title" : title,
        "region" : region,
        "location" : location,
        "link" : link,
    }


def stackover_page_change(num):
    view_companys = list()
    for page in range(1, num+1):
        stackover_result = requests.get(f'{URL}&pg={page}')
        stackover_soup = BeautifulSoup(stackover_result.text, 'html.parser')
        companys = stackover_soup.find_all('div',{"class":"-company"})
        for company in companys:
            view_company = company_info(company)
            view_companys.append(view_company)
    return view_companys


def stackover_get_job():
    last_num = stackover_last_pn()
    return stackover_page_change(last_num)