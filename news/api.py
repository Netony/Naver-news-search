import urllib.request
import json
from time import sleep

client_id = "LYVZkqjtCMSsIoNTSvbo"
client_secret = "Nd46m_umMZ"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    data = response_body.decode('utf-8')  
    item = json.loads(data)
    print(type(item))

    print(item)
else:
    print("Error Code:" + rescode)