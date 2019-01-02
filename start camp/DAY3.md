# DAY3

___

## 1. Dictionary

***

> Dictionary는 `key`와 `value`가 짝지어져있다.

key는 `string`, `integer`, `boolean` 가능하다. `list` 혹은 `dictionary`는 안된다.

`value`는 모든 자료형이 가능하다. `list` 혹은 `dictionary`도 가능하다.

### 1) 딕셔너리 만들기

```python
phonebook = {
    "중국집" : "021561561"
}
phonebook2 = dic(중국집=021561561)
```

### 2) 딕셔너리 내용 추가하기

```python
phonebook["분식집"] = "031"
```

### 3) 딕셔너리 내용 가져오기

```python
idol = {
    "BTS" : {
        "지민": 24,
        "RM": 25
    }
}
# 랩몬스터의 나이는?
idol["BTS"]["RM"]
```

### 4) 딕셔너리 반복문 활용하기

```python
# 기본 활용
for key in phonebook:
    print(key)
    print(phonebook[key])

# .items()
for key, value in phonebook.values():
    print(value)
```



## [연습문제](https://zzu.li/dj_dict1)

```python
# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
'''
for person_score in score.values():
    for individual_score in person_score.values():
        total_score += individual_score
        length += 1
average_score = total_score / length
print(avrage_score)
'''
z = 0
x = 0
for iusum in score["iu"].values():
    z = z + iusum
for uisum in score["ui"].values():
    x = x + uisum
c = z + x
num = len(score["iu"]) + len(score["ui"])
avr = c / num
print(avr)
```



## 텔레그램 API 활용하기

___

> 사전 준비사항 : @botfather를 통해서 봇을 만들어서 토큰 정보를 기록한다.

### 1. 봇정보 가져오기

```python
https://api.telegram.org/bot{token}/getME
```

```python
import requests
token = "토큰"
url = f"https://api.telegram.org/bot{token}/getMe"
response = requests.get(url)
```

### 2. 메세지 보내기

(1) user의 `id`를 가져와야함

```python
https://api.telegram.org/bot{token}/getUpdates
```

```python
import requests

# 1. 사용자 정보 가져오기 위한 요청
token = "토큰"
url = f"https://api.telegram.org/bot{token}/getUpdates"
response = requests.get(url).json()

# 2. 사용자 정보 및 메세지 설정
user_id = response["result"][0]["message"]["from"]["id"]
msg = "안녕안녕?"

# 3. 메세지 보내기
send_url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"
requests.get(url)
```

!!주의사항

token은 반드시 외부에 공개되면 안된다.

따라서, 환경변수를 활용해서 내 컴퓨터에만 정보를 저장한다.

```powershell
$ vi ~/.bash_profile
export TELEGRAM_TOKEN='토큰정보'
```

```python
import os
token = os.getenv("TELEGRAM_TOKEN")
```

