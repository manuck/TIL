# Django (template language)

---

## urls 설정

```python
path('home/template_example/', views.template_example),
```



## views 설정

```python
def template_example(request):
    my_dict = {'name': 'Noh', 'nickname': 'manuck', 'age': 26}
    my_list = ['짜장면', '짬뽕', '탕수육', '양장피']
    my_sentence = 'Life is short, you need python!'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    now = datetime.datetime.now()
    return render(request, 'template_example.html',{'my_list':my_list, 'my_dict':my_dict, 'my_sentence':my_sentence, 'messages':messages, 'now':now})
```

---



## template_example

### 1. 반복문

```django
{% for menu in my_list %}
    {{ forloop.counter }} <!-- for루프 카운트 출력 -->
    {% if forloop.first %} <!-- for루프 처음에만 -->
        <p>짜장면 + 고추가루</p>
    {% else %}
        <p>{{ menu }}</p>
    {% endif %}
{% endfor %}
{% for user in empty_list %}
    <p>{{ user }}</p>
    {% empty %}  <!-- 비어있음	 -->
        <p>지금 가입된 유저가 없습니다.</p>
{% endfor %}
```

```
1
짜장면 + 고추가루

2
짬뽕

3
탕수육

4
양장피

지금 가입된 유저가 없습니다.
```



### 2. 조건문

```django
{% if '짜장면' in my_list %}
    <p>짜장면은 고추가루 없이 못 먹지!</p> <!-- if 리스트 안에 있으면 -->
{% endif %}
```

```
짜장면은 고추가루 없이 못 먹지!
```



### 3. length filter 활용

```django
{% for message in messages %}
    {% if message|length > 5 %} <!-- 길이가 5글자 넘어가면 -->
        <p>글씨가 너무 길어요</p>
    {% else %}
        <p>{{ message }}</p>
    {% endif %}
{% endfor %}
```

```
apple

글씨가 너무 길어요

글씨가 너무 길어요

mango
```



### 4. lorem ipsum

```django
{% lorem %} <!-- 아무 장문 -->
<hr>
{% lorem 3 w %} <!-- 앞에서 3단어 -->
<hr>
{% lorem 3 w random %} <!-- 3 단어 랜덤 -->
<hr>
{% lorem 4 p %} <!-- 4문단 -->
```

```
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

lorem ipsum dolor

odit quae accusamus

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Qui officiis dignissimos placeat ex porro, voluptatum ab ex debitis ipsam pariatur velit eius quos, consectetur corporis aspernatur doloremque earum beatae voluptas expedita itaque, voluptatem dignissimos voluptas modi optio itaque ipsa, error similique deserunt aliquam eum dignissimos sed?

Eligendi hic animi aperiam accusantium incidunt libero dolorum labore, et reiciendis nihil aliquam doloremque est maxime fuga debitis, similique tempora cupiditate voluptatibus doloremque corrupti a velit quos ratione molestias amet. Atque culpa quo odio perspiciatis nesciunt consequuntur fuga nobis, aliquid non qui officia, labore doloribus ab accusantium corrupti recusandae repudiandae? Quasi accusantium debitis soluta dolorum in iste sapiente architecto earum, consequuntur minima vitae, dolor quisquam blanditiis?

Nobis repudiandae dolor nemo odit delectus voluptates expedita quis dicta, dignissimos officia facere quisquam voluptatem alias quam deleniti vitae autem asperiores.
```



### 5. 글자수 제한하기(truncate)

```django
<p>{{ my_sentence|truncatewords:3 }}</p> <!-- 3단어 이후 ... -->
<p>{{ my_sentence|truncatechars:10 }}</p> <!-- 10개 글자수인데 ...과 공백 모두 포함 -->
```

```
Life is short, ...

Life i ...
```



### 6. 글자 관련 필터

```django
<p>{{ 'abc'|length }}</p> <!-- 글자수 출력 -->
<p>{{ 'ABC'|lower }}<p>  <!-- 소문자로 -->
<h3>{{my_sentence|title }}</h3>  <!-- 타이틀식으로 -->
<p>{{ 'abc def. hi'|capfirst }}</p> <!-- 첫글자만 대문자 -->
<p>{{ my_list|random }}</p> <!-- 리스트에서 랜덤 -->
```

```
3

abc

Life Is Short, You Need Python!
Abc def. hi

양장피
```



### 7. 연산 (django-mathfilters 쓰면 추가적으로도 가능하긴함.)

```django
<p>{{ 4|add:6 }}</p> <!-- 더하기 -->
```

```
10
```



### 8. 날짜표현

```django
{{now}} <br>  <!-- 날짜 표기(시간포함) -->
{% now "SHORT_DATETIME_FORMAT" %}<br> <!-- 짧은 날짜표기 -->
{% now "DATETIME_FORMAT" %}<br> <!-- 날짜 표기(시간포함) -->
{% now "DATE_FORMAT" %}<br> <!-- 날짜 표기(시간제외) -->
{% now "Y년 m월 d일 (D) h:i" %}<br> <!-- 날짜 표기 (요일도 표시) -->
```

```
2019년 2월 12일 11:37 오전 
2019-2-12 11:37
2019년 2월 12일 11:37 오전
2019년 2월 12일
2019년 02월 12일 (화요일) 11:37
```



### 추가

```django
{{ 'http://google.com'|urlize }}
```

