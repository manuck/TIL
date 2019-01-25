# README

---

## 1. 영화진흥위원회 오픈 API(주간/ 주말 박스오피스데이터)

```python
key = os.getenv('kobis_key')
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    url = f"{url}?key={key}&targetDt={targetDt[i]}&weekGb={weekGb}&"
    response = requests.get(url).json()
    a = (response['boxOfficeResult']['weeklyBoxOfficeList'])
```

을 통하여 url을 불러서 데이터값을 확인하고 

```python
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['영화코드', '영화명','총누적','해당일']
    write = csv.DictWriter(f, fieldnames= fieldnames)
    write.writeheader()
    for k in result.values():
        write.writerow(k)
```

을 통하여 csv 파일에 '영화코드', '영화명','총누적','해당일'로 나눠 저장한다.

---

## 2. 영화진흥위원회 오픈 API(영화 상세정보)

1번 파일을 Read해서 할 수 있지만 1번에서 뽑은것을 바로 읽어서 만들었다.

```python
url2 = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    url2 = f"{url2}?key={key}&movieCd={nom[j]}&"
    response2 = requests.get(url2).json()
    b = (response2['movieInfoResult']['movieInfo'])
```

```python
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['영화코드','영화명(국)','영화명(영)', '영화명(원)', '개봉연도', '상영시간', '장르', '감독명','관람등급','배우1','배우2','배우3']
    write = csv.DictWriter(f, fieldnames= fieldnames)
    write.writeheader()
    for k in no2.values():
        write.writerow(k)
```

fieldnames 에 있는 내용으로 csv 파일을 생성

---

## 3. 네이버 영화

```python
client_id = os.getenv('naver_id')
client_secret = os.getenv('naver_secret')
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
url = 'https://openapi.naver.com/v1/search/movie.json?' 
```

통해서 네이버 API 정보를 가져오고

```python
with open('movie.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie3 = {}
        movie_name=row['영화명(국)']
#         print(movie_name)
        movie_code=row['영화코드']
        m_url = f"{url}query={movie_name}"
        response = requests.get(m_url, headers=headers).json()
#         pprint.pprint(response)
        movie_info = response['items'][0]
        movie3['영화코드'] = movie_code
        movie3['썸네일'] = movie_info['image']
        movie3['하이퍼링크'] = movie_info['link']
        movie3['평점'] = movie_info['userRating']
        result[row['영화코드']] = movie3
        time.sleep(0.1)
```

통해 movie.csv 파일을 read해서 movie_naver.csv 파일을 생성한다.

시간 에러가 발생하기 때문에 time.sleep으로 시간을 늦췄다.

---

## 4. 스크린샷

```python
with open('movie_naver.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie4 = {}
        movie_code=row['영화코드']
        movie_sum=row['썸네일']
        s_url = f'{movie_sum}'
        if s_url:
            with open(f'./images/{movie_code}.jpg' ,'wb') as f:
                img = requests.get(s_url).content
                f.write(img)
```

네이버 영화 내용중 '썸네일' 을 찾아서 이미지를 영화코드.jpg로 저장했다.

