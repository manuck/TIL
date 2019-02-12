# C9 setting

---

## 1.pyenv 설정

---

> pyenv는 하나의 컴퓨터 내에서 여러가지 버전의 python을 활용할 수 있도록 버전관리를 도와준다.
>
> pyenv global : 전체 전역 파이썬 버전 설정
>
> pyenv local : 해당 디렉토리 파이썬 버전 설정

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
python -V
```





## 2. pyenv-virtualenv

---

> virtualenv는 독립적인 가상환경을 제공해준다.
>
> 가장 많이 활용되는 3가지 라이브러리는 다음과 같다.
>
> 1. pyenv-virtualenv : pyenv의 플러그인
> 2. virtualenv
> 3. conda : 데이터사이언스/머신러닝/딥러닝

```bash
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
```

## 

## 실행

```
pyenv virtualenv 3.6.7 {가상환경 이름}
pyenv local {가상환경이름}
```

```
ex)
pyenv virtualenv 3.6.7 flask-venv
pyenv local flask-venv
```



## 3. Git

---

> c9은 기본적으로 workspace에서 git config가 가입한 이메일로 되어 있기 때문에, github에 커밋 기록을 제대로 남기기 위해서 설정해준다.

```bash
git config --global user.name manuck
git config --global user.email snc9000@naver.com
```

---

## Django

```
pyenv virtualenv django-venv
pyenv local django-venv

django-admin startproject #django_intro(프로젝트 이름)
```

