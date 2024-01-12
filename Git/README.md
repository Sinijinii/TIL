2024년 1월 11일 

참고

https://naon.me/posts/til46 

https://git-scm.com/book/ko/v2

---

- 변화를 기록하고 추적하는 것
- 버전을 여러개의 복제된 저장소에 저장 및 관리
- 중앙 서버에 의존하지 않고도 동시에 작업을 수행할 수 있음

---

## 📌목차
🟡깃의 역할

🟡Git의 3가지 영역 

    1. Working Directory
    2. Staging Area
    3. Repository

🟡깃 사용법

    1. 기본 작업 흐름
    2. 원격 저장소에 만들어진 브랜치 로컬로
    3. 임시저장만(**커밋 메시지x**)
    4. 실수 시
    5. 기타 참고

🟡커밋 메시지 컨벤션

---

## 🟡깃의 역할

- 코드의 버전(히스토리)를 관리
- 개발되어 온 과정 파악 == 발정과정을 알 수 있음
- 이전 버전과의 변경 사항 비교 가능
- 코드의 변경 이력을 기록하고 협업을 원활하게 하는 도구

---

## 🟡Git의 3가지 영역

### 1. Working Directory

- 내가 작업하고 있는 프로젝트의 디렉토리

### 2. Staging Area

- Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역

### 3. Repository

- 버전 이력과 파일들이 영구적으로 저장되는 영역
- 모든 버전과 변경 이력이 기록

![이미지](https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F1848a85f-9836-46e1-8795-3eff9f43f933%2Fd20718b9-fcc9-48ae-9059-320d4a1d4afa%2FUntitled.png?table=block&id=bdcac465-a550-4208-9eff-23a396e5daca&spaceId=1848a85f-9836-46e1-8795-3eff9f43f933&width=2000&userId=c47d7f68-ac31-480d-b4eb-cf60fb57b9e1&cache=v2)

Staging Area에 추가한 파일들을Commit을 한다면 최종적으로 저장소(Repository)로  저장

- git init
    - 주의 사항: git 로컬 저장소 내에 또 다른 git 로컬 저장소를 만들면 안됨 - 에러도 안남
    - 디렉토리 내부 하단에 중복 init하면 안됨 - rm-rf .git
    - 가장 바깥쪽의 git 저장소가 안쪽의 git 저장소의 변경 사항을 추적할 수 없기 때문
- git add
    - Staging Area에 추가하는 코드
    - add “.” > 전체 파일
- git commit
    - repository에 올리는 코드
    - add된 내용만 올라감
    - commit에는 commit message필요

---

## 🟡깃 사용법

### **기본 작업 흐름**

1. 최초 프로젝트 시작 시 원격저장소 마스터를 내 로컬 마스터로 복사 (master에 이미 다른 팀원이 최신 파일을 올려두었다는 가정 하) 
    - `git clone 마스터 브랜치 주소`
2. 로컬 마스터를 복사해서 마찬가지로 내 로컬에 브랜치 생성. 즉, 브랜치 생성 = 현재 로컬 마스터를 브랜치에 복사
    - `git branch 브랜치이름`
3. 해당 브랜치에서 작업 완료 후 혹은 중간중간 원격저장소에 push
    - `git add .` : 스테이징(”.” > 전체/ git add test.txt > 특정 파일)
    - `git commit` : 에디터로 커밋 메시지 작성 (git commit -m “메시지”)
    - `git push origin 브랜치이름` : 마스터로 푸시 X. 반드시 브랜치로 푸시
4. 해당 브랜치 github 페이지에서 Pull request
5. 검토가 끝나고 마스터와 merge가 되면 내 로컬 마스터로 이동해서 pull 받아옴. 
    
    이때 작업 중이던 것은 commit까지 해두고 pull 받아와야 함
    
    - `git add .git commit` : 작업 내용 임시저장까지 완료한 후 pull
    - `git checkout master`
    - `git pull origin master`
6. 작업하던 것과 싱크를 맞춰야 하므로 작업하던 브랜치로 이동해서 내 로컬 마스터 내용과 merge 해줌
    - `git checkout 브랜치이름`
    - `git merge master` : 여기서 master는 원격저장소의 master가 아니라 내 로컬을 말함
7. 충돌(conflict) 메시지에 따라서 파일 수정.
    
    꼭 수정 후 바로 push하지 않아도 괜찮지만, push할 준비가 된 브랜치에 한해 `git merge master`를 해주는 게 좋음
    
    - `git add .`
    - `git commit`
    - `git push origin 브랜치이름`

### **원격 저장소에 만들어진 브랜치 로컬로**

1. 원격 저장소 변경사항 업데이트`git remote update`
2. 원격 저장소의 모든 브랜치 보기`git branch -a`
3. feature/modeling 이라는 브랜치 가져오기`git checkout -t origin/feature/modeling`

### **임시저장만(**커밋 메시지x)

1. 현재 작업 내용을 임시 저장
    - `git add .`
    - `git stash`
2. 임시 저장한 작업 내역을 다시 불러옴
    - `git stash apply [stash 이름]`
3. 작업 완료 후에는 보통 푸시와 과정 동일
    - `git add .`
    - `git commit`
    - `git push origin 브랜치이름`
4. 작업 끝난 내용의 stash 제거하기. 가장 최근 stash 하나를 제거
    - `git stash drop`
5. apply와 동시에 stash를 제거
    - `git stash pop`
6. stash를 잘못 불러온 경우
    - `git stash show -p | git apply -R`혹은`git stash show -p [stash 이름] | git apply -R`

### 실수 시

1. 커밋 취소
- `git reset --soft HEAD^`
    - 커밋을 취소하고 변경 사항을 staged 상태로 돌림 (add까지 한 상태로)
- `git reset --mixed HEAD^`
    - 커밋을 취소하고 변경 사항을 unstaged 상태로 돌림 (add 이전 상태로)
- `git branch -d 브랜치이름`
    - 브랜치 삭제
1. 커밋 메시지 수정
- `git commit --amend`
    - **가장 마지막에 commit 한 내용** 수정
    - 커밋을 수정할 수 있는 창이 뜨면, 수정을 완료한 후 `esc` -> `:wq`(저장 + 창 닫기)
- `git rebase -i HEAD~n`
    - n개 전의 메시지
        
        > pick | 커밋 번호 | 커밋 메시지
        > 
        - 형식으로 출력
    - `pick`이라는 문구를 `reword`로 바꿔주고 `esc` - `:wq` 진행

### **기타 참고**

- Pull request(PR) 날린 후 merge 대기 상태에서 계속 push 하면 commit이 누적 > 나중에 한꺼번에 merge 가능하다. merge 기다리면서 같은 브랜치에서 계속 작업 가능
- merge 전 새 브랜치 파서 작업하려면 우선 내 로컬 마스터로 이동한 후에 새 브런치를 만들어어 줘야함.
    - `git checkout mastergit pull origin master` : 혹시 적용해야할 변경사항이 없는지 확인
    - `git branch 새브랜치이름git checkout 새브랜치이름` : 이동 후 새 작업 시작
- 브랜치 이동 시 반드시 add - commit 혹은 stash까지 하고 이동해야 함
    - 잘못하면 다른 브랜치와 작업 내용이 섞일 수 있음
- `git log`확인 후 터미널 커서로 빠져나오기: Q
- CLI에서 코드 여는 방법: `code .`

---

# 🟡커밋 메시지 컨벤션

# **Git - Commit Message Convention**

커밋 메시지를 작성할 때는 원칙을 정하고 일관성 있게 작성하기 위해 만들어진 구조

## **1. Commit Message Structure**

기본적으로 커밋 메시지는 제목/본문/꼬리말로 구성

```
type : subject

body

footer
```

## **2. Commit Type**

- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- refactor : 코드 리펙토링
- test : 테스트 코드, 리펙토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정

## **3. Subject**

- 제목은 50자를 넘기지 않고, 대문자로 작성하고 마침표 사용하지 않음
- 과거시제를 사용하지 않고 명령어로 작성
    - "Fixed" --> "Fix"
    - "Added" --> "Add"

## **4. Body**

- 선택사항이기 때문에 모든 커밋에 본문내용을 작성할 필요는 없음
- 부연설명이 필요하거나 커밋의 이유를 설명할 경우 작성
- 72자를 넘기지 않고 제목과 구분되기 위해 한칸을 띄워 작성

## **5. footer**

- 선택사항이기 때문에 모든 커밋에 꼬리말을 작성할 필요는 없음
- issue tracker id를 작성할 때 사용