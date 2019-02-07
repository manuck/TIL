# 190207

---

## ORM(flask-sqlalchemy)

---

1. 기본 설정

   ```bash
   $ pip install flask_sqlalchemy flask_migrate
   ```

   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy
   from flask_migrate import Migrate
   
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
   db = SQLAlchemy(app)
   
   
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)
   
       def __repr__(self):
           return '<User %r>' % self.username
   ```

   

2. flask db 설정

* 초기 설정(`migration` 폴더 생성)

   ```bash
   $ flask db init
   ```

* migration 파일 생성

   ```bash
   $ flask db migrate
   ```

* db반영

   ```bash
   $ flask db upgrade
   ```

   

3. 활용법

   1) Create

   ```python
   # user 인스턴스 생성
   user = User(username='이재찬', email='lee@gmail.com')
   # db.session.add 명령어를 통해 추가
   # INSERT INTO user (username, email)
   # VALUES ('이재찬', 'lee@gmail.com');
   db.session.add(user)
   # db에 반영
   db.session.commit()
   ```

   2) READ

   ```python
   # SELECT * FROM user;
   users = User.query.all()
   # get 메소드는 primary key로 지정된 값을 통해 가져온다.
   user = User.query.get(1)
   # 틍정 컬럼의 값을 가진 것을 가져오려면 다음과 같이 쓴다.
   user = User.query.filter_by(username='이재찬').all()
   user = User.query.filter_by(username='이재찬').first()
   ```

   3) UPDATE

   ```python
   user = User.query.get(1)
   user.username = '홍길동'
   db.session.commit()
   ```

   4) DELETE

   ```python
   user = User.query.get(1)
   db.session.delete(user)
   db.session.commit()
   ```

   

4. Base Template

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
</head>

<body>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
            <div class="alert alert-{{category}}" role="alert">
                  {{message }}
            </div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
    </nav>
    <div class="container mt-5">
        {% block body %}
        {% endblock %}
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>

```

5. Child Template

```html
{% extends 'base.html' %}

{% block title %}
회원 명부
{% endblock %}

{% block body %}
    <h2>{{username}}</h2>
    <h2>{{email}}</h2>
{% endblock %}
```

---

### app.py

```python
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.secret_key = 'asdjasdbkad'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30))
    created_at = db.Column(db.String(80), nullable=False)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now().strftime("%D")

    def __repr__(self):
        return f'{self.id}: {self.username}'
        
        
@app.route('/')
def index():
    users = User.query.all()
    # type(users) : list 타입
    # list element: user 인스턴스
    return render_template('index.html', users=users)
    
@app.route('/users/new')
def new_user():
    return render_template('new.html')

# 두가지는 완전 다른 요청이다!
# GET /users/create
# POST /users/create

@app.route('/users/create', methods=["POST"])
def create_user():
    username = request.form.get('username') # 이재찬
    email = request.form.get('email') #lee@lee
    # user = User(username='이재찬', email='lee@lee')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return render_template('create.html', username=user.username, email=user.email)
    
@app.route('/users/read/<int:id>')
def read_user(id):
    user = User.query.get(id)
    return render_template('read.html', user=user)
    
@app.route('/users/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash(f'{user.username}이 삭제되었습니다.', 'warning')
    return redirect('/')
    
@app.route('/users/edit/<int:id>')
def edit_user(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)

@app.route('/users/update/<int:id>', methods=["POST"])
def update_user(id):
    user = User.query.get(id)
    user.username = request.form.get('username')
    user.email = request.form.get('email')
    db.session.commit()
    flash('수정되었습니다.', 'success')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8080', debug = True)
```

### index.html

```html
{% extends 'base.html' %}
{% block title %}
회원 명부
{% endblock %}
{% block body %}
    <h1>회원 명부</h1>
    <ul>
        {% for user in users %}
            <p></p>{{user.id}}: {{user.username}}</p>
            <p>{{user.email}}</p>
            <a href="/users/read/{{user.id}}">상세보기</a>
            <a href="/users/delete/{{user.id}}">삭제하기</a>
            <a href="/users/edit/{{user.id}}">수정하기</a>
            <hr>
        {% endfor %}
    </ul>
{% endblock %}
```

### new.html

```html
{% extends 'base.html' %}

{% block title %}
회원가입 폼
{% endblock %}

{% block body %}
    <form action='/users/create', method="POST">
        username : <input type="text" name="username"> <br>
        email : <input type="email" name="email"> <br>
        <input type="submit" value = "회원가입">
    </form>
{% endblock %}
```

### create.html

```html
{% extends 'base.html' %}
{% block title %}
회원 명부
{% endblock %}
{% block body %}
    <h2>{{username}}</h2>
    <h2>{{email}}</h2>

{% endblock %}
```

### read.html

```html
{% extends 'base.html' %}

{% block title %}
회원 명부
{% endblock %}

{% block body %}

<h1>{{user.id}}: {{user.username}}</h1>
<p>{{user.email}}</p>
<p>{{user.created_at}}</p>

{% endblock %}
```

### edit.html

```html
{% extends 'base.html' %}

{% block title %}
회원 수정
{% endblock %}

{% block body %}
    <form action='/users/update/{{user.id}}', method="POST">
        username : <input type="text" name="username" value="{{user.username}}"> <br>
        email : <input type="email" name="email" value="{{user.email}}"> <br>
        <input type="submit" value = "수정">
    </form>

{% endblock %}

```
sadsadsad

## 암호화

```bash
$ pip install werkzeug
```

```python
from werkzeug.security import generate_password_hash, check_password_hash
a = 'hihi'

#암호화
hash = generate_password_hash(a)
print(hash)
#차이점 확인
check_password_hash(hash, 'hihi')
check_password_hash('hihi', hash)
```

