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

    
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['영화코드', '영화명','총누적','해당일']
    write = csv.DictWriter(f, fieldnames= fieldnames)
    write.writeheader()
    for k in result.values():
        write.writerow(k)