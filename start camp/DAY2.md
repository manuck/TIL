# DAY2

___

## 스크래핑 기초

___

### 1) 설치

```powershell
$ pip install requests
$ pip install bs4
```

* `requests` : 요청을 대신 보내준다.
* `bs4` [링크](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): 문서를 파싱하는 것을 도와준다.

## 2) 코스피 지수 가져오기

1. 네이버에서 증권 페이지를 요청한다.
2. 페이지에서 내가 찾고 싶은 내용을 찾는다.

```python
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
#1. 원하는 사이트에 요청을 보낸다. 그리고, 그 결과를 response에 저장한다.
response = requests.get(url)

#2. 컴퓨터가 이해하는 방식으로 변환(text -> html)
soup = BeautifulSoup(response.text, 'html.parser')
# #KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.

#3. 원하는 정보를 CSS selector를 활용하여 가져오기
kospi =  soup.select_one('#KOSPI_now')

#4. 출력하기
print(kospi.text)
```











## 2. HTML/CSS

___

### 1) HTML

HTML은 HyperText Markup Language의 약자로, 웹문서에서 활용이 된다.

웹 문서의 구조와 내용을 담당한다.

```html
<!Doctype html>
<html>
    <head>
        /*문서의 정보를 담고있다 */
        <title>탭 이름</title>
        <style>
            /* 클래스가 red */
            .red {
                color:red;
            }
            /* id가 blue */
            #blue {
                color: blue;
            }
            /* 태그가 p */
            p {
                color: skyblue; 
            }
            /* !important붙이면 무조건 우선1순위 */
        </style>
    </head>

    <body>
        /*문서의 내용을 담고있다. 실제로 브라우저에서 보이는 내용이 여기에 해당 */
    <!-- 우선순위 = 인라인 > id > class > tag -->
    <!-- 인라인(inline) 속성 -->
        <h1 id = "blue" style="color:red;">안녕? 제목이니?</h1>
        <h2 class="red">아닛? 빨간색?</h2>
        <p id="blue" class="red">빨간색? 파란색?</p>
        <p id="blue">파랑이좋겠군</p>
        <p>하늘색</p>
    </body>
    
</html>
 

```



### 2) CSS

CSS는 Cascading Style Sheets의 약자로 HTML과 같은 마크업 언어를 꾸며주는 역할을 한다.

꾸며주기 위해서 특정한 태그를 선택해야하는데 이때 활용되는 것이 `CSS 선택자(selector)`라고 부른다.

* `id` : #
* `class` : .
* `tag` 

```html
<html>
    <head>
        <style>
            /* 클래스가 red */
            .red {
                color:red;
            }
            /* id가 blue */
            #blue {
                color: blue;
            }
            /* 태그가 p */
            p {
                color: skyblue; 
            }
            /* !important붙이면 무조건 우선1순위 */
        </style>
    </head>

    <body>
        <h1 style="color:red;">인라인 속성</h1>
        <h2 class="red">클래스적용</h2>
        <p id="blue" class="red">파란색</p>
        <p id="blue">ID적용</p>
        <p>태그</p>
    </body>
    
</html>
```





## 3. 파일 조작

---

### 1.  `os` 외장함수

```python
import os

#1. 내가 원하는 위치로 이동
os.chdir(r'경로')

#2. 해당 디렉토리 내에 있는 파일명 가져오기 - ls
files = os.listdir()

#3. 파일명 바꾸기
for file in files:
    os.rename(file, "지원자"+file)
```



### 2. file 열어서 조작하기

#### 1) 기본사용법

```python
with open("파일명", "w") as file:
    file.write("글써짐")
    
with open("파일명", "r") as file:
    line = file.read()
    print(line)
```

파일 조작하는 모드는 다음과 같다.

* w : write(덮어쓰기)
* r : read(읽기)
* a : append(이어쓰기)

#### 2) 파일읽기

```python
# 1. read() : 전체를 하나의 string
line = file.read() # 전체 내용

# 2. readline() : 한줄씩 string으로 가져옴
line = file.readline() # 첫 번째 줄
line = file.readline() # 두 번째 줄

# 3. readlines() : 전체를 하나의 list, element는 한줄의 string
lines = file.readlines()
for line in lines:
    print(line.strip('\n')) # 공백제거
```

