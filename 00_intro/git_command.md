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
  * 