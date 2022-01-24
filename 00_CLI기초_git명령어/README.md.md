### CLI 기초

---

`_` : 스페이스바 대신 표시

`<string>` : string만 입력함 

ex) `cd_<Desktop>` 의 경우 cd desktop 만 실제 입력/ 대소문자 구분 X

---

* `clear` : 코드 정리. 깨끗한 화면으로 돌아감

* `pwd` : 현재 나의 위치(경로) 확인
* `ls` : 현재 경로에 있는 파일 및 폴더 리스트 확인
* `cd_<경로>` : 경로로 이동
  * `/` 로 구체적으로 경로 지정 가능
  * ex)`cd desktop/new/new2` 경우 데스크탑 폴더 안의 new 폴더 안의 new2 폴더까지 한번에 이동가능
*  `cd_..` :  상위 폴더로 이동
  * ex)위 경우를 예로 들면 new로 이동됨
* `mkdir_<폴더이름>` : 폴더를 생성, 바로 이동되지는 않음// 이동하려면 `cd_<폴더이름>`으로 이동 가능
* `vi_<파일이름>` : 같은 이름을 가진 파일이 있다면, 수정모드 없다면 생성 후 수정 모드로 진입
  * 이후 `i` 버튼으로 입력모드 전환
  * `esc`키로 입력모드 탈출
  * `:w` : 저장하기
  * `:q`  나가기
  * `:wq` 저장 후 나가기
* `touch_<파일이름>` : 해당 이름을 가진 파일 생성
* `start_<파일이름.확장자>` : 해당 파일 실행
* `rm_<파일이름.확장자>` :해당 파일 삭제
* `rm_-r_<폴더이름>` : 해당 폴더 삭제
* `mv_<기존폴더이름>_<새폴더이름>` : 기존폴더이름을 새폴더 이름으로 변경
* `mv_<기존파일.확장자>_<폴더>` : 기존파일위치를 폴더 위치로 변경

---

### 유용한 단축키

* `위,아래 방향키`: 이전 명령어들 조회
* `tab`: 이름 검색 및 조회, 과거 명령어 조회
* `ctrl+a` : 커서가 맨 앞으로 이동
* `ctrl+e` : 커서가 맨 뒤로 이동
* `ctrl+w`:  커서가 맨 앞 단어를 삭제
* `ctrl+l`  clear랑 같은 기능이지만, 스크롤 올리면 과거 조회 가능
* `ctrl+insert` : 터미널 문장 복사 
* `shift+insert`: 터미널에 문장 붙여넣기

---

## git 명령어 모음

* **내 컴퓨터에서 최초로 깃-깃허브 매핑시켜줄 때**
  * username, pw
  * chrome
    * git/django,javascript,vue
    * `git config --global user.name "username"` : username 등록
    * `git config --global user.email <email>` : email 등록
* **Working Directory(내 로컬 폴더)**  **1회**
  * `git init` : 깃과 최초 연결하기(.git폴더가 생성됨)
  * `git remote add origin <레포주소>`: 레포 연결
* **Staging Area(.git폴더)** **필요할 때마다**
  * `git remote` : remote 별명 확인
  * `git remote -v` : remote 주소 확인
  * `git add .` : "내 모든 파일들 올려줘" 
  * `git add 파일.확장자 파일2.확장자` : 파일과 파일2만 올려줘
  * `git status` : 현재 깃과의 상태 확인 가능, 깃과 연결되어 있는지, 어느 깃에 연결되어있는지 등등 
  * `git commit -m "할 말"` : 할 말로 커밋해줘
* **깃헙에 push하기**
  * git push -u origin master` : 최초 push 때만,마스터 저장소로 보내줘(저장해줘)
* **git pull하기** **<복제 + master에 수정도 가능(권한 있을 경우)>**
  * pull 해 올 폴더 생성
  * 해당 폴더에 `git init` 한 다음
  * `git remote add origin <주소>`  : 해당 주소와 깃을 연결한다는 뜻
  * `git pull origin master` : 해당 주소 파일을 다 가져옴
* **git clone하기** **<해당 상태 그대로 복제>**
  * clone파일 저장할 폴더생성
  * 해당 폴더에 `git init`  한 다음
  * `git clone <가져올 주소>` : 해당 파일 가져오기 
  * **CLIF오류 떴을 때**(깃헙에서 맥인지 윈도우인지 헷갈려서 나타나는 오류)
    * `git config --global core.autocrlf true` 입력하면 끝
* **커밋 내역 확인 + 커밋 고유번호 확인 가능**
  * `git log` : 커밋 히스토리 상세 확인
  * `git log oneline` : 커밋 히스토리 간략 확인 

---

# lab으로 협업 시작하기

* `git init` 으로 깃 시작
* 지역변수 설정하기(로컬 유저 등록)
  * `git config --local user.name 'username'` : 으로 로컬 유저 등록
    * 유저 확인은 `git config --local user.name` 입력으로 확인 가능
  * `git config --local user.email 'email'` 으로 로컬 이메일 등록
    * 이메일 확인은 `git config --local user.email` 입력으로 확인 가능

* 깃 연결하기
  * `git remote add origin <연결주소>` :로 연결
  * `git remote -v`  : 어디에 연결되었는지 확인
  * **pull 할 때**  (지속적인 업데이트로 계속해서 pull할 상황이 있을 때)
    * `git pull origin master` 로 땡겨오기
  * **clone할 때** (깃헙에 있는 자료를 가져올 때)
    * `git clone <연결주소>` : 로 복사해옴