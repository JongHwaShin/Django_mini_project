# KBO Player Project

## Django mini project

-------------------------


* 목차
    * 개발목적
    * 기능
    * Model 구성
    * 화면

### 개발목적
``` 
1. KBO 선수들의 정보를 저장하고 조회 할 수 있다.
2. 직접 선수의 이름,팀,포지션,연봉,연도,타율/방어율 등을 저장 할 수 있다.
3. 저장한 선수들의 연봉 순위를 확인 할 수 있다.
4. 팬은 선수에 대한 댓글을 통해 선수를 응원 할 수 있다.
5. KBO 공식 사이트에 나와있는 투수,타자 Top30,Top20을 세분화된 기록과 함께 확인 할 수 있다.


```  

### 기능

기능 | 세부기능          | 세부요구사항                           | 전제조건                    
------|---------------|----------------------------------|-------------------------|
리스트 | 등록된 선수 리스트 조회 | 사용자가 등록한 선수 전체 리스트를 조회한다.        | 사용자가 선수를 사전에 등록해야 한다.   |
선수추가| 새로운 선수 추가     | 사용자는 선수의 정보(이름,팀,포지션,연봉,연도,타율/방어율) 를 등록한다. | 선수에 대한 상세 정보가 존재 하여야한다. |
상세정보| 선수 상세 정보 조회         | 사용자는 등록을 마친 선수의 정보를 조회 한다.       | 사용자가 선수의 모든 정보를 등록완료 해야 한다.                    |
선수 수정| 등록한 선수 정보 수정      | 사용자는 등록한 선수의 정보를 수정하고 저장할 수 있다.| 정보를 빠짐없이 입력하여 등록 된 선수가 존재하여야한다.
선수 삭제| 등록한 선수 삭제    | 사용자는 등록한 선수를 삭제할 수 있다.| 사전에 등록된 선수가 존재하여야한다.
댓글 달기 | 선수에 대한 댓글 달기     | 작성자는 선수에 대한 댓글을 작성할 수 있다.| 작성자 이름과 댓글 내용이 입력되어야 한다.
연봉 순위 | 등록된 선수의 연봉 순위 조회     | 등록된 선수의 연봉에 따라 정렬후 순위를 붙혀 조회 가능하다.| 선수 등록시 연봉 정보를 반드 시 입력하여야 한다.
TOP |타자 TOP30 투수 TOP20 조회 가능   | KBO 페이지에서 가져온 선수 타자 TOP30,투수 TOP20 정보를 DB 에 저장한후 페이지에 가져온다. | 정보는 KBO 페이지를 웹스크래 핑 한 후 DB 에 저장되어 있어 야한다.


### Model 구성

* class Kboplayer  // 등록선수
  * name  // 이름
  * team  // 팀
  * position  // 포지션
  * year_moeny // 연봉
  * year // 연도
  * created_date // 작성 날짜
  * update_date  // 업데이트 날짜
  * attack_or_attacked // 타율 or 방어율
  

* class Comment //댓글
  * player_post // 댓글을 등록한 선수 글
  * author // 작성자
  * text // 댓글 내용
  * created_date // 작성 날짜


* class Player   // Database에서 가져올 KBO 타자 Top30 을 위한 모델
  * 순위
  * 선수명
  * 팀명
  * avg // 타율
  * g   // 게임수
  * pa // 타석
  * ab // 타수
  * r  //득점
  * h  // 1루타
  * number_2b // 2루타
  * number_3b // 3루타
  * hr // 홈런
  * tb // 루타
  * rbi // 타점
  * sac // 희생타
  * sf // 희생플라이


* class Player2   // Database에서 가져올 KBO 투수 Top30 을 위한 모델
  * 순위
  * 선수명
  * 팀명
  * era // 평균자책점
  * g  // 게임
  * w  // 승
  * l  // 패
  * sv // 세이브
  * hld // 홀드
  * wpct // 승률
  * ip // 소화 이닝
  * h  // 피안타
  * hr // 피홈런
  * bb // 볼넷
  * hbp // 사구 or 몸에맞는볼
  * so // 삼진
  * r  // 실점
  * er // 자책점
  * whip // 인닝당 출루허용률
  
### 화면
 
* 등록선수 list 및 조회 
 
<img width="1239" alt="등록 선수 list 조회 및 홈화면" src="https://user-images.githubusercontent.com/98075696/163549744-70cecbdd-92a7-4383-95dd-bf3380cb6e5f.png">

* 선수 등록

<img width="1194" alt="선수등록" src="https://user-images.githubusercontent.com/98075696/163550024-de07cffb-2f44-41ed-bc5b-fe49156c2055.png">


* 선수 상세정보 조회 및 댓글 확인

<img width="1269" alt="선수 상세정보 조회 및 댓글 확인" src="https://user-images.githubusercontent.com/98075696/163550139-9c0bf452-38af-4a1a-b75d-6979dc1132b6.png">

* 댓글 작성

<img width="1263" alt="댓글작성" src="https://user-images.githubusercontent.com/98075696/163550170-d2243a16-d532-4351-b018-a3df7d52cd06.png">

* 등록 선수 연봉 순위 확인

<img width="1241" alt="등록 선수 연봉 순위 확인" src="https://user-images.githubusercontent.com/98075696/163550215-1f0db809-1454-43d1-b3d7-5e0c523cd8da.png">

* 타자 TOP 30 조회


<img width="1332" alt="타자 TOP 30 조회(1)" src="https://user-images.githubusercontent.com/98075696/163550285-3194ce69-18bf-42f8-b859-fd7ec825aef8.png">


<img width="1221" alt="타자 TOP 30 조회 (2)" src="https://user-images.githubusercontent.com/98075696/163550353-e3e9bb75-6d56-4cd1-a508-1fa60dea11c2.png">


* 투수 TOP 20 조회


<img width="1288" alt="투수 TOP 20 조회 (1)" src="https://user-images.githubusercontent.com/98075696/163550408-eae91507-123c-496e-aad9-f72fce6e8ea9.png">
<img width="1217" alt="투수 TOP 20 조회 (2)" src="https://user-images.githubusercontent.com/98075696/163550434-bd1870f7-290b-4b79-a6e1-916ff85c1708.png">


### DB 테이블 구성

* 등록 선수 테이블 

<img width="1056" alt="등록 선수 테이블" src="https://user-images.githubusercontent.com/98075696/163550511-03ff7e05-e683-45c4-bb6d-72ad87922abf.png">

* 댓글 테이블

<img width="935" alt="댓글 테이블" src="https://user-images.githubusercontent.com/98075696/163550550-7fc1d634-c378-4ae6-be61-1b4297604b3b.png">

* 타자 TOP 30 테이블

<img width="1019" alt="타자 TOP 30 테이블" src="https://user-images.githubusercontent.com/98075696/163550583-c343bf74-4f9c-45b0-b136-7397304e9df2.png">

* 투수 TOP 20 테이블

<img width="1133" alt="투수 TOP 20 테이블" src="https://user-images.githubusercontent.com/98075696/163550642-7b6e6fc0-4c77-4ac2-ac53-f43de192b4bc.png">


