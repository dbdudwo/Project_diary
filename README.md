# 나만의 개인 다이어리 일기장 7log
개인의 일상을 기록하고 공유하는 다이어리 제작
<br><br>
<br>
## 프로젝트 기획
- 많은사람들이 어릴 떄 그림일기를 작성해본 경험이 있을 텐데 그걸 토대로 요즘 시대에 맞춰 그림대신 사진을 넣고 다이어리 형식의 일기장을 만들기로함

<br><br>
## 프로젝트 구조
![image](https://user-images.githubusercontent.com/100177702/158132413-1f2bb7c0-4675-41f7-ba51-f115cf41ea6a.png)
- 장고의 MVT형식을 이용함
<br>

## 프로젝트 정보
### 환경설치(필수)
아나콘다 환경에서 장고 설치
```
conda install django
```
mysql 모듈 설치
```
pip install mysqlclient
```
부트스트랩 설치
```
pip install django-bootstrap4
```
파이썬 이미지 처리를 위한 pillow 서리
```
pip install pillow
```

### 개발 환경 및 사용 기술
개발 언어
```
Python,HTML,CSS,JavaScript
```
framework
```
Django
```
## 프로젝트 초기 구성
### 메인페이지, 로그인 페이지, 회원가입 페이지
![image](https://user-images.githubusercontent.com/100177702/158135638-913a06a2-2173-4d50-95a8-518204768a5a.png)

- 메인 페이지 : 검색기능 및 [About, How to user, Dashboard]에 대한 간략한 설명을 볼 수 있고 상단의 로그인 버튼을 통해 로그인을 진행할 수 있음
<br>

- 로그인 페이지 : 로그인 페이지로 이동시 아이디와 비밀번호를 입력하여 로그인을 진행할 수 있고 추가적으로 회원가입 및 id/pw찾기 기능구현예정
<br>

- 회원가입 페이지 : 회원가입페이지는 각각의 입력상자를 통해 사용자에게 값을 입력 받아 회원가입을 진행 할 수 있도록 구성

<br><br>

### About, Dashboard 페이지
![image](https://user-images.githubusercontent.com/100177702/158135408-5c1427d6-01d9-403f-b935-4739df963849.png)

- About 페이지 : 상단의 메뉴바의 어바웃 페이지의 경우 7log의 간단 소개글을 볼 수 있음
<br>

- Dashboard : 대쉬보드 페이지로 이동시 7log에 작성된 게시글을 확인 할 수 있음

<br><br>

### 새글작성, 게시글 상세보기 페이지
![image](https://user-images.githubusercontent.com/100177702/158135847-3886b0b4-547a-43dc-be5b-83fd157c9b4f.png)

- 새글작성 페이지 : 새글작성 시 이미지, 지도, 제목, 사용자명, 내용이 들어감
<br>

- 상세보기 페이지 : 작성된 게시글의 상세보기를 통해 좋아요 및 수정, 삭제, 댓글 기능을 구현예정

<br><br>


## 프로젝트 결과물
기능 및 결과 예시 화면
<br>
### 메인페이지
