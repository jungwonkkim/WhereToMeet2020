import requests
import json


kakao_key = '발급받은 키'
kakao_url = '/v2/local/search/address.json'
kakao_host = 'https://dapi.kakao.com'
kakao_headers = {'Authorization': f'KakaoAK {kakao_key}'}

#주소의 x좌표를 출력하는 함수
def searchx(location):
    myurl = kakao_host + kakao_url + f'?query={location}'
    response = requests.get(myurl, headers=kakao_headers).text
    response = json.loads(response)
    return float(response['documents'][0]['address']['x'])

#주소의 y좌표를 출력하는 함수
def searchy(location):
    myurl = kakao_host + kakao_url + f'?query={location}'
    response = requests.get(myurl, headers=kakao_headers).text
    response = json.loads(response)
    return float(response['documents'][0]['address']['y'])

kakao_url_key = '/v2/local/search/keyword.json'
#주소의 키워드를(존재한다면 출력하는 함수)
def keyword(location):
    myurl = kakao_host + kakao_url_key + f'?query={location}'
    response = requests.get(myurl, headers=kakao_headers).text
    response = json.loads(response)
    return response



#최단거리 spot을 구하는 함수 
def time(array):
    spots = {
    '강남역': (127.028000275071, 37.4980854357918),
    '사당역': (126.981558584016, 37.4765604303289),
    '홍대입구': (126.923778562273, 37.5568707448873),
    '잠실역': (127.100228759082, 37.513312862699),
    '용산역': (126.964824061815, 37.5300763645794),
    '건대입구': (127.069202917341, 37.5404084182632),
    '천호역': (127.12392845044, 37.5385112120297),
    '왕십리': (127.027518075708, 37.5646082774221),
    '역삼역': (127.03646946847, 37.5006744185994),
    }

    OD_key = '발급받은 key'
    my_time_min = 1000000
    my_stn = ""
    for stn in spots.keys():
        SX = spots[stn][0]
        SY = spots[stn][1]
        my_time = 0        
        for person in array:
            EX = person[0]
            EY = person[1]
            OD_url = f'https://api.odsay.com/v1/api/searchPubTransPathR?lang=0&SX={SX}&SY={SY}&EX={EX}&EY={EY}&apiKey={OD_key}'
            response = requests.get(OD_url).text
            response = json.loads(response)
            my_time += response['result']['path'][0]['info']['totalTime']
            if my_time > my_time_min:
                break
        if my_time < my_time_min:
            my_time_min = my_time
            my_stn = stn
    
    return (my_time_min, my_stn, spots[my_stn])