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