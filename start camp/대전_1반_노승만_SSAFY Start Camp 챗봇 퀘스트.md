# SSAFY Start Camp 챗봇 퀘스트

---

## 1. 스펙(Specification)

---

구현된 어플리케이션의 주요 기능 작성

### 1) 메아리

* 사용자가 텔레그램을 통해 챗봇에게 문자를 입력
* 챗봇인 문자를 인식하고 같은 메세지를 보냄

### 2) 로또

* 사용자가 텔레그램을 통해 챗봇에게 `로또`라는 채팅을 입력
* 챗봇이 `로또`를 인식하여 로또번호 6자리를 추천해줌

### 3) 번역

* 사용자가 텔레그램을 통해 챗봇에게 `/번역_______`라는 채팅을 입력
* 네이버 API 이용하여 한글 채팅 내용일 경우, 영어로 번역하여 채팅옴

### 4) 유명인 인식(닮은꼴)

* 사용자가 텔레그램을 통해 챗봇에게 `사진`을 입력
* 네이버 API 이용하여 데이터가 이미지일 경우, 닮은 연예인과 닮은 정도를 표현

---

## 2. 회고(Retrospective)

---

어플리케이션 구현 과정에서의 어려움과 문제점

* 크롤링을 배울 때 예시로 `실시간 검색어 순위` or `코스피 지수` 및 `미세먼지 지수`를 가져오는 것을 했는데 딕셔너리에서 찾는 것을 주의 깊게 해야 오류가 발생하지 않아서 신경써야한다.
* `토큰`과  `id`를 저장시키는 것도 주의깊게 해야한다.
* `BeautifulSoup`과 `json`의 구별도 알아둬야 한다.

---

## 3. 보완 계획(Feedback)

---

현재 미완성이지만 추가로 구현할 기능 및 기존 문제점 보완 계획

### 1) 미세먼지 기능

* `미세먼지` 를 입력시, 현재 대전 지역의 미세먼지 지수를 가져오는 기능을 추가적으로 개발하고 싶다.

### 2) 실시간 검색어

* `실시간` 입력시  상위 5개 정도의 실시간 검색어 순위가 표시되는 기능을 추가적으로 개발하고 싶다.