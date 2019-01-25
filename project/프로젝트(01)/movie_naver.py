import requests
import os
import pprint
import csv
import time

client_id = os.getenv('naver_id')#여기에 발급받은 id 입력해주세요(네이버 id아님)
client_secret = os.getenv('naver_secret')#여기에 발급받은 secret 입력해주세요.
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
url = 'https://openapi.naver.com/v1/search/movie.json?' #여기에 영화 검색 API의 url을 만들어주세요.
# mm='말모이'
# m_url = f'{url}query={mm}'
# response = requests.get(m_url, headers=headers).json()
# pprint.pprint(response)

result = {}
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
        
pprint.pprint(result)