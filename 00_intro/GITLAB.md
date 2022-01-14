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
