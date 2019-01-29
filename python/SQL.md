# SQL

---

## 1. 데이터베이스(DB)

> 데이터베이스는 체계화된 데이터의 모임이다.



### 1.1 RDBMS(관계형데이터베이스 관리 시스템)

> 관계형 모델을 기반으로하는 데이터베이스 관리시스템이다. 아래는 대표적인 오픈소스 RDBMS(MySQL, SQLite, PostgreSQL)과 ORACLE, MS SQL이다.

### 1.2 SQLite

>SQLite는 서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다. 구 안드로이드 운체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용이 되고 있다. 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용할 수 있다. 

---

### 용어정리

스키마(scheme) : 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조.

---



## SQL

>SQL(Structured Query Language)는   관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다. 관계형 데이터베이스 관리 시스템에서 자료의 검색과 관리   데이터베이스 스키마 생성과 수정, 데이터베이스 객체 접근 조정 관리를 위해 고안되었다.

|                        |                             개념                             |              예시              |
| :--------------------: | :----------------------------------------------------------: | :----------------------------: |
|  DDL-데이터 정의 언어  | 데이터를 정의하기 위한 언어이다. <br/>관계형 데이터베이스 구조(테이블, 스키마)를 
정의하기 위한 명령어이다. |      CREATE<br/>DROP
ALTER      |
| DML - 데이터 조작 언어 |   데이터를 저장, 수정, 삭제, 조회 등을 하기 위한 언어이다.   | INSERT<br/>UPDATE
DELETE
SELECT  |
| DCL - 데이터 제어 언어 |  데이터베이스 사용자의 권한 제어를 위해 사용되는 언어이다.   | GRANT<br/>REVOKE
COMMIT
ROLLBACK |

---

### 1.SELECT

```
SELECT * FROM table 
```

```
sqlite> .headers on 
sqlite> .mode column 
```

### 조회

```
.tables 
.schema table
```

### 2. DROP

```
DROP TABLE table 
```

### 테이블 만들기

```
sqlite> CREATE TABLE classmates (
id INT PRIMARY KEY,  
name TEXT, 
age INT,  
address TEXT 
); 
```

---

### 데이터 추가 (INSERT)

```
INSERT INTO table (column1, column2,..) VALUES (value1, value2, …) 
```

### 데이터 가져오기(SELECT)

```
SELECT column1, column2 FROM table
```

```
LIMIT num
```

```
LIMIT num OFFSET num
```

```
WHERE column=value
```

### 데이터 삭제(DELETE)

```
DELETE FROM table WHERE condition 
```

```
DELETE FROM table WHERE id=?
```

### 데이터 수정 (UPDATE)

```
UPDATE table SET column1=value1, column2=value2, … WHERE condition 
```

### 개수반환

```
SELECT COUNT(column) FROM table
```

### 평균,합,최소,최대

```
SELECT AVG(column) FROM table [ AVG(), SUM(), MIN(), MAX() ]
```

### LIKE(패턴을 확인하여 값을 반환)

```
WHERE column LIKE 2% OR _2%
```

|  %   |  2%   |               2로 시작하는 값                |
| :--: | :---: | :------------------------------------------: |
|      |  %2   |                2로 끝나는 값                 |
|      |  %2%  |               2가 들어가는 값                |
|  -   |  _2%  | 아무값이나 들어가고 두번째가 2로 시작하는 값 |
|      |  1__  |           1로 시작하고 4자리인 값            |
|      | 2_%_% |        2로 시작하고 적어도 3자리인 값        |



### 정렬(ORDER)

```
SELECT columns FROM table ORDER BY column1, column2 [ASC|DESC]
```

