# django-User

# 190408

django_fbv



1. 유저만들기(admin)

   ```bash
   python manage.py createsuperuser
   ```

2. shell_plus

`settings.py`

```python
INSTALLED_APPS = [
    'django_extensions',	# 추가
]
```

```bash
$ python manage.py shell_plus
```

```shell
>>>Uuser = get_user_model()
>>> User.objects.all()
<QuerySet [<User: sungmin>, <User: manuck>]>
```



> 버전 설치

pip install django==2.1.5



---



1. App생성

```bash
$ python manage.py startapp accounts
```

2.`settings.py` 에 추가

```python
INSTALLED_APPS = [
    'accounts',
]
```

3. `urls.py`(django_fbv)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```

4. `urls.py` 생성(accounts)

   ```
   from django.urls import path
   from . import views
   
   
   app_name = 'accounts'
   urlpatterns = [
       path('signup/', views.signup, name='signup'),
       path('login/', views.login, name='login'),
       path('logout/', views.logout, name='logout'),
   ]
   ```

5. `forms.py` 생성

   ```python
   from django import forms
   from django.contrib.auth import get_user_model
   
   class UserForm(forms.ModelForm):
       class Meta:
           model = get_user_model()
           # fields = '__all__'
           fields = ['username', 'password']
   ```

   

6. `views.py`(signup)

   ```python
   import pprint
   from django.shortcuts import render, redirect
   # from .forms import UserForm
   from django.contrib.auth import login as auth_login
   from django.contrib.auth import logout as auth_logout
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib.auth.decorators import login_required
   
   def signup(request):
       if request.user.is_authenticated:
           return redirect('boards:index')
       
       if request.method == "POST":
           user_form = UserCreationForm(request.POST)
           if user_form.is_valid():
               user = user_form.save()
               auth_login(request, user)
               return redirect('boards:index')
       else:
           user_form = UserCreationForm()
       context = {"user_form": user_form}
       return render(request, 'accounts/signup.html', context)
       
   ```

7. templates 폴더생성(폴더내에 accounts폴더 추가 생성)

8. templates 안에 `signup.html` 파일 생성 (회원가입)

   ```html
   {% extends 'boards/base.html' %}
   {% block body %}
   {% load crispy_forms_tags %}
   <form method="POST">
       {% csrf_token %}
       {{ user_form|crispy }}
       <input type='submit' value="회원가입 신청">
   </form>
   {% endblock %}
   ```

9. `views.py`(login)

   ```python
   def login(request):
       if request.user.is_authenticated:
           return redirect('boards:index')
           
       if request.method == "POST":
           login_form = AuthenticationForm(request, request.POST)
           if login_form.is_valid():
               auth_login(request, login_form.get_user())
               return redirect('boards:index')
       else:
           login_form = AuthenticationForm()
       context = {'login_form': login_form}
       return render(request, 'accounts/login.html', context)
   ```

10. templates 안에 `login.html` 파일 생성 (로그인)

    ```html
    {% extends 'boards/base.html' %}
    {% block body %}
    {% load crispy_forms_tags %}
    <form method="POST">
        {% csrf_token %}
        {{ login_form|crispy }}
        <input type='submit' value="로그인">
    </form>
    {% endblock %}
    ```

11. `base.html` 수정

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>FBV</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <body>
        {% if user.is_authenticated %}
            <h1>{{ user }}님 반갑습니다.</h1>
            <a href="{% url 'accounts:logout' %}">로그아웃</a>
        {% else %}
            <a href="{% url 'accounts:signup' %}">회원가입</a>
            <a href="{% url 'accounts:login' %}">로그인</a>
        {% endif %}
        {% block body %}
        {% endblock %}
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>
    ```

12. `views.py` (logout)

    ```python
    @login_required
    def logout(request):
        auth_logout(request)
        return redirect('boards:index')
    
    ```
---
# 190409

1. `urls.py`(accounts)

   ```python
       path('delete/', views.delete, name='delete'),
       path('update/', views.update, name='update'),
       path('password/', views.password, name='password'),
   ```

2. `views.py`(accounts)

   ```python
   @login_required
   def logout(request):
       auth_logout(request)
       return redirect('boards:index')
   
   @login_required
   @require_http_methods(["POST"])
   def delete(request):
       request.user.delete()
       return redirect('boards:index')
   
   # @login_required
   # def delete(request):
   #     if request.method == 'POST':
   #         request.user.delete()
   #     return redirect('boards:index')
   
   @require_http_methods(["GET", "POST"])
   def update(request):
       # user_form = UserChangeForm()
       if request.method == 'POST':
           user_form = UserCustomChangeForm(request.POST, instance=request.user)
           if user_form.is_valid():
               user_form.save()
               return redirect('boards:index')
       else:
           user_form = UserCustomChangeForm()
       context = {'user_form':user_form}
       return render(request, 'accounts/update.html', context)
       
   @login_required
   def password(request):
       if request.method == 'POST':
           user_form = PasswordChangeForm(request.user, request.POST) # 순서 주의!
           if user_form.is_valid():
               user = user_form.save()
               update_session_auth_hash(request, user)
               return redirect('boards:index')
       else:
           user_form = PasswordChangeForm(request.user) # instance= 아님 주의!
       context = {'user_form':user_form}
       return render(request, 'accounts/update.html', context)
   ```

3. `accounts`에 `forms.py` 생성

   ```python
   from django import forms
   from django.contrib.auth import get_user_model
   from django.contrib.auth.forms import UserChangeForm
   # class UserForm(forms.ModelForm):
   #     class Meta:
   #         model = get_user_model()
   #         # fields = '__all__'
   #         fields = ['username', 'password']
   
   class UserCustomChangeForm(UserChangeForm):
       class Meta:
           model = get_user_model()
           fields = ['email', 'first_name', 'last_name',]
   
   ```

4. `update.html`생성

   ```python
   {% extends 'boards/base.html' %}
   {% block body %}
   {% load crispy_forms_tags %}
   <form method="POST">
       {% csrf_token %}
       {{ user_form|crispy }}
       <input type='submit' value="프로필 수정">
   </form>
   {% endblock %}
   ```

5. `boards`에서 `base.html` 에 추가

   ```html
   <a href="{% url 'accounts:update' %}">프로필수정</a>
           <!--<a href="{% url 'accounts:delete' %}">회원탈퇴</a>-->
           <form action="{% url 'accounts:delete' %}" method="POST" onsubmit="return confirm('탈퇴할꺼야?')">
               {% csrf_token %}
               <input type="submit" value="회원탈퇴">
           </form>
   ```

>1 : N 
>
>user : board

---

1. `boards`에서 `models.py`수정

   ```python
   # from django.contrib.auth.models import User # 사용하지 마세요
   # from django.contrib.auth import get_user_model 
   from django.conf import settings
   # settings.AUTH_USER_MODEL
   
   # Create your models here.
   class Board(models.Model):
       # 아래코드 추가
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ```

2. `boards`에서 `views.py` 수정

   ```python
   @login_required
   def create(request):
       # if not request.user.is_authenticated:
       #     return redirect('boards:index')
       
       if request.method == 'POST':
           board_form = BoardForm(request.POST)
           if board_form.is_valid():
               # title = board_form.cleaned_data.get('title')
               # content = board_form.cleaned_data.get('content')
               # board = Board(title=title, content=content)
               # board.user = request.user
               # board.save()
               board = board_form.save(commit=False)
               board.user = request.user
               board.save()
               return redirect(board)
       else:
           board_form = BoardForm()
       context = {'board_form': board_form}
       return render(request, 'boards/form.html', context)
   ```

3. migration과 migrate 다시하기

   ```bash
   $ python manage.py makemigrations
   ```

   이미 있는 db와 달라서 질문이 들어온다

   ```bash
   You are trying to add a non-nullable field 'user' to board without a default; we can't do that (the database needs something to populate existing rows).
   Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit, and let me add a default in models.py
    
   Select an option: 1
   
   Please enter the default value now, as valid Python
   The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
   Type 'exit' to exit this prompt
   >>> 
   Please enter some code, or 'exit' (with no quotes) to exit.
   >>> 1
   ```

   ```bash
   $ python manage.py migrate
   ```

4. `detail.html` 수정

   ```html
   {% extends 'boards/base.html' %}
   
   {% block body %}
   <h1>{{ board.pk }}번째 글</h1>
   <h2>{{ board.title }}</h2>
   <h3>작성자 : {{ board.user }}</h3>
   <p>조회수 : {{ board.hit }}</p>
   <hr>
   <p>{{ board.content }}</p>
   <!--작성자와 user와 일치시에만 수정과 삭제가 표시되게 -->
   {% if board.user == user %}
   <a href="{% url 'boards:update' board.pk %}"><input type="submit" value="수정"></a>
   <form action="{% url 'boards:delete' board.pk %}" method="POST">
       {% csrf_token %}
       <input type="submit" value="삭제">
   </form>
   {% endif %}
   {% endblock %}
   ```

   