import requests
import os
import csv

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