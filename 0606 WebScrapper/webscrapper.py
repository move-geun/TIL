import requests
from bs4 import BeautifulSoup

# 주소 가져오기
indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")

# 오류 없는지 확인
# print(indeed_result)    # <Response [200]>
# print(indeed_result.text)

# bs4가 공식문서 참고(사용법)

# 페이지만 뽑아오기
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

page_ul = indeed_soup.find("ul", {"class":"pagination-list"})
page_lis = page_ul.find_all("li")

page = list()
for page_li in page_lis:
    link = page_li.select('a > span', {"class":"pn"})

    if link:
        page.append(link)

page = page[:-1]
print(page)
