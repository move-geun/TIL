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


def stackover_page_change(num):
    for page in range(1, num+1):
        stackover_result = requests.get(f'{URL}&pg={page}')
        stackover_soup = BeautifulSoup(stackover_result.text, 'html.parser')
        companys = stackover_soup.find_all('div',{"class":"-company"})
        for company in companys:
            print(company.find("a",{"class":"s-link"}).string)


last_num = stackover_last_pn()
stackover_page_change(last_num)