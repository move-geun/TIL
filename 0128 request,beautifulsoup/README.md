### 파이썬을 활용한 데이터 수집 II

---

#### 프로젝트 안내

* 외부 데이터를 수집하여 원하는 결과를 도출하기
  * 인기 영화 조회
  * 특정 조건에 맞는 인기 영화 조회
  * 특정 영화 추천 영화 조회
  * 특정 영화 배우, 감독 리스트 조회

---

#### 웹 스크래핑(웹 크롤링)

##### - 요청(클라이언트/url)과 응답(서버/html,xml,json)

* ##### requests : simple HTTP library for Python. (파이썬을 위한 라이브러리)

  * CLI에서 `pip install requests`

* ##### BeautifulSoup : html and xml 파일에서 데이터 가져오는 라이브러리

  * CLI에서 `pip install beautifulsoup4`

```python
# 웹 사이트의 정보를 가져오고 싶다.
import requests
from bs4 import BeautifulSoup


# 1-1. 주소
URL = 'https://finance.naver.com/sise/'
# 1-2. 요청
# response [200] == 성공적으로 가져왔다는 뜻
response = requests.get(URL).text
# print(type(response)) => 'str'

# 2-1. BeautifulSoup (text -> 다른 객체로 변환)
# html 파일에서 내가 원하는 데이터를 가져오기 위해서 활용
data = BeautifulSoup(response,'html.parser')
# print(type(data)) => <class 'bs4.BeautifulSoup'>
# 2-2. 내가 원하는 정보를 찾는다
# 선택자 활용!
kospi = data.select_one('#KOSPI_now') #select_ont() => 원하는 거 하나만 뽑겠다
print(kospi.text) # 2,594.14


```

---

#### API (Application Programming Interface)

* 컴퓨터나 프로그램 사이의 연결
* 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공

##### - 활용법

* 요청하는 방식에 대한 이해
  * 인증 방식
  * URL 생성
    * 기본 주소
    * 원하는 기능에 대한 추가 경로
    * 요청 변수(필수와 선택)
* 응답 결과에 대한 이해
  * 응답 결과 타입(JSON)
  * 응답 결과 구조

```python
import requests

# 1. URL
# 요청변수 : ?name=michael
#URL = 'https://api.agify.io?name=michael'
URL = 'https://api.agify.io'
parmas = {
    'name' : 'haley',
}
# 2. 요청 (현재 파일은 json파일로 바로 오기 때문에 beautifulsoup 사용할 필요 x)
# requests에서 제공하는 .json 활용
response = requests.get(URL,params=parmas).json()
print(response.get('age')) # 36
```

---

##### 예제 실습

```python
# 0. import
import requests
from pprint import pprint
# 1. URL 및 요청변수 설정
# https://developers.themoviedb.org/3/movies/get-now-playing
# http로 요청보낼거야, 주소가 있고 그 주소에 요청 파라미터에 값이 있어!
# https://api.themoviedb.org/3/movie/now_playing?api_key=8854669b886a6c07c12ea947bcc2311d&region=KR&language=ko
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
box = {
    'api_key' : 'secret_code_I_cant_show_this',
    'region' : 'KR',
    'language' : 'ko',
}

# 2. 요청 보낸 결과 저장
response = requests.get(BASE_URL+path, params=box).json()
pprint(response)     # 결과 데이터 꺼냄

#------------------------------------------------------------#

# 2-1. 다른 방법
response = requests.get(BASE_URL+path, params=box) #.json()
print(response.status_code, response.url) # 200, 404  같은 상태코드, 직접 url 제공
data = response.json() 
print(data)             # 결과 데이터 꺼냄

# 3. 하나씩 꺼내 보기 조작...
print(type(data))  # dict
print(data.keys()) # ['dates', 'page', 'results', 'total_pages', 'total_results']
print(type(data.get('results'))) # list
print(data.get('results')[0]) #results의 첫번째 값
print(len(data.get('results'))) # results는 20개의 값을 가지고 있다
```

