import requests
import os
import csv

key = os.getenv('kobis_key')
# url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
result ={}
movie = []
targetDt = [20190113, 20190106, 20181230, 20181223, 20181216, 20181209, 20181202, 20181125, 20181118, 20181111]
weekGb = "0"
for i in range(10):
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    url = f"{url}?key={key}&targetDt={targetDt[i]}&weekGb={weekGb}&"
    response = requests.get(url).json()
    a = (response['boxOfficeResult']['weeklyBoxOfficeList'])
    for j in range(len(a)):
        if  a[j]['movieCd'] not in result:
            movieN = {}
    #         if movieN[j]['영화코드'] == a[j]['movieCd']:
    #             break
    #         else:
            movieN['영화코드'] =  a[j]['movieCd']
            movieN['영화명'] =  a[j]['movieNm']
            movieN['해당일'] =  targetDt[i]
            movieN['총누적'] = a[j]['audiAcc']
            result[a[j]['movieCd']]=movieN
# print(result)
nom = list(result.keys())
no2 = {}
for j in range(len(result)):            
    url2 = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    url2 = f"{url2}?key={key}&movieCd={nom[j]}&"
    response2 = requests.get(url2).json()
    b = (response2['movieInfoResult']['movieInfo'])

    for i in range(len(b)):
        movieM = {}
        movieM['영화코드'] = b['movieCd']
        movieM['영화명(국)'] = b['movieNm']
        movieM['영화명(영)'] = b['movieNmEn']
        movieM['영화명(원)'] = b['movieNmOg']
        movieM['개봉연도'] = b['prdtYear']
        movieM['상영시간'] = b['showTm']
        movieM['장르'] = b['typeNm']
        movieM['감독명'] = b['directors'][0]['peopleNm']
        movieM['관람등급'] = b['audits'][0]['watchGradeNm']
        if len(b['actors']) == 1 : 
            movieM['배우1'] = b['actors'][0]['peopleNm']
        elif len(b['actors']) == 2 : 
            movieM['배우1'] = b['actors'][0]['peopleNm']
            movieM['배우2'] = b['actors'][1]['peopleNm']
        elif len(b['actors']) >= 3 : 
            movieM['배우1'] = b['actors'][0]['peopleNm']
            movieM['배우2'] = b['actors'][1]['peopleNm']
            movieM['배우3'] = b['actors'][2]['peopleNm']
        
        no2[b['movieCd']] = movieM 
print(no2)

#     print(result)
    
# with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
#     fieldnames = ['영화코드', '영화명','총누적','해당일']
#     write = csv.DictWriter(f, fieldnames= fieldnames)
#     write.writeheader()
#     for k in result.values():
#         write.writerow(k)


with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['영화코드','영화명(국)','영화명(영)', '영화명(원)', '개봉연도', '상영시간', '장르', '감독명','관람등급','배우1','배우2','배우3']
    write = csv.DictWriter(f, fieldnames= fieldnames)
    write.writeheader()
    for k in no2.values():
        write.writerow(k)