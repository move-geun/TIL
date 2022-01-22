### 파이썬을 활용한 데이터 수집 

* Python 기본 문법 실습
* 파일 입출력에 대한 이해
* 데이터구조에 대한 분석과 이해
* 데이터를 가공하고 JSON형태로 저장
* JSON 데이터를 원하는 결과물로 변환

---

#### JSON 파일 open 방법

* `open(file, mode='r', encoding=None)` 

* ```python
  f = open('workfile', 'w')
  ```

* ```python
  whith open('workfile') as f :
  	read_data = f.read()
  f.closed
  ```

* JSON : 문자 기반 데이터 포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능함

  * 텍스트를 언어별 데이터 타입으로 변환시키거나, 언어별 데이터 타입을 적절하게 텍스트로 변환

  * ```python
    #객체를 json으로 변환
    import json
    x = [1, 'simple']
    json.dumps(x)
    '[1, "simple"]'
    ```

    ```python
    #json을 객체로 변환
    x= json.load(f)
    ```

* `Pprint`

  * ```python
    #많은 양의 자료를 이쁘게 출력
    from pprint import pprint
    ```

* `dict.get(key,default)` : 딕셔너리 접근 방법 (에러가 뜨지 않음)

  ![image-20220121111918224](https://user-images.githubusercontent.com/85543481/150532598-2a1c9488-4976-4804-8577-ad2e2a56630e.png)

* `dict['a']` : 위와 같이 key를 통해 value를 찾지만, 요소가 없는 경우 keyerror 발생됨

---
