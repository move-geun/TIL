### 명세서 구조

* **목표**
* **준비사항**
  * 개발언어/프로그램, 라이브러리, 외부 데이터 등
* **요구사항**
  * 제시된 요구사항에 맞춰 개발 진행
* **결과**
  * 반드시 결과로 나타난 폴더 구조를 참고하여 작성

---

### GIT

* 분산 버전 관리 시스템  중 하나
* 컴퓨터 파일의 변경사항을 추적, 여러 사용자들간 파일 작업율 조율
* `개인과제_최최최최초치ㅗ치최최초치ㅚㅊ종.pdf` 와 같은 버전 관리에 용이
* 하나의 파일이지만 버전을 기록, 확인 가능 / 이전 상태 확인 가능
* DVCS (분산버전관리시스템)
  * 새로운 버전을 생성,  모든 히스토리를 공유, 중앙 서버가 터져도 다양한 복구 방법이 있음
  * `<-> `CVCS (중앙집중식버전관리시스템) : 중앙 서버에서 필요한 것만 가져와 업데이트하는 예전 방법

---

### Git Bash

* 윈도우에서 Git을 활용하기 위한 기본 도구, 기본 프롬프트

* Command Line Interface(CLI) : 명령 기반의 인터페이스

  * CLI로써, 사용자와 컴퓨터가 상호 작용하는 방식
  * 키보드를 통해 문자열의 형태로 작업 명령 입력

  ![image-20220121092431976](https://user-images.githubusercontent.com/85543481/150729134-3520ac65-9a1d-4481-94ef-61ce6f88b3b8.png)

  * GUI : 그래픽 기반의 인터페이스 `<-> ` CLI

  ![image-20220121092541726](https://user-images.githubusercontent.com/85543481/150729161-742d1b70-fad8-4ef0-9643-8a5150bdc6ef.png)

* **Git bash 명령어** (여러 터미널에서 사용가능하지만 터미널 종류에 따라 호환되지 않는 것도 일부 있음)

  * *'<', '>'는 입력하지 않습니다.  ex)`cd desktop` 과 같이 입력.*
  * `ls` : 현재 폴더에 있는 파일 또는 폴더 목록 출력
  * `mkdir <폴더명>` : '폴더명'의 폴더 생성
  * `cd <폴더명>`: 폴더명으로 이동
  * `cd ..`: 현재 폴더의 상위폴더로 이동
  * `pwd` : 현재 나의 위치 확인
  * `touch <파일명>` : '파일명'의 파일 생성
  * `vi <파일명>` : '파일명'을 가진 파일이 있다면 수정모드, 없다면 생성 후 수정모드 진입
  * `rm <파일명.확장자>` : '파일명'의 파일 삭제
  * `rm -r <파일명.확장자>` : 해당 파일 또는 폴더와 그 하위 파일 및 폴더 모두 강제 삭제 

---

### Git 기초 흐름

1. **Working Directory(내가 작업 중인 디렉토리)**
2. **Staging Area(버전 기록을 위한 변경사항의 목록, .git 폴더)**
3. **Repository(커밋들이 기록되는 곳)**

#### 	1. Git 저장소 생성(깃 기초흐름 1번)

* git으로 관리하려는 폴더에서 `git init`

* 해당 폴더에 .git 폴더가 생성되는데 건드리면 안됨
* .git 폴더 삭제시 git 연결 끊는것과 같은 의미

#### 	2. Staging Area로 이동(.git 폴더)

* `git status` : 현재 폴더의 변경 내역 확인 가능(수정되었는지, add 되었는지)
* 파일 변경 후 `git add .`
* `git commit -m '변경사항'` : 변경사항으로 커밋이 기록됨
* `git log` : 커밋 로그와 고유 해시값 확인 가능
* `git log -oneline` : 로그 요약본 확인 가능

####  	3.  Repository로 이동

* `git push -u <원격저장소> <branch>` : 쌓여있던 커밋 기록들을 레포로 보냄
  * ex) a,b 파일 커밋 후, c 파일을 따로 커밋 한 다음, git push를 하면 두개의 커밋이 push 됨

---

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
