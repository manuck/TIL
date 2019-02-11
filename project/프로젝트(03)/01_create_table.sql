CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' INTEGER,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
-- 출력 방식 설정
.headers on
.mode column
-- csv 데이터 가져오기
.mode csv
.import boxoffice.csv movies
-- 전체 데이터 출력하기
SELECT * FROM movies;