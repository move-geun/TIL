#### Git branch

##### master 브랜치

- 중심이 되는 브랜치
- 원본을 보관하는 곳
- 상용됨(실제로 서비스가 되거나 될 코드)

##### branch command

- `git branch` : 브랜치 목록 확인
- `git branch <브랜치 이름>` : 새로운 브랜치 생성
- `git branch -d <브랜치 이름>` : 특정 브랜치 삭제
- `git branch -D <브랜치 이름>` : merge 안 된 상태의 git branch 삭제
- `git switch <브랜치 이름>` : 브랜치 이름으로 이동
- `git switch -c <브랜치 이름>` : 브랜치를 생성과 동시에 이동
- `git log --oneline --all` : master를 포함한 모든  branch의 로그 상태를 한 줄로 확인
- `git log --oneline --all --graph` : 그림 형태로 보여줌



##### merge

* `git merge <병합할 브랜치 이름>`
  * merge하기 전에 병합할 메인 브랜치로 switch 되어야 함

1. fast-forward
2. 3-way merge(merge commit)
3. merge conflict
   * merge하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면, git은 해당 부분을 자동으로 merge 해주지 못함
   * 반면 동일 파일이더라도 서로 다른 부분을 수정했다면, conflict 없이 자동으로 merge commit 된다.