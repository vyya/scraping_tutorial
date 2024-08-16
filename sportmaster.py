import requests
from bs4 import BeautifulSoup

url = 'https://sportmaster.kz/ru/catalog/'

headers = {
'accept' : '*/*',
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
      (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
req = requests.get(url, headers = headers)
src = req.text
#print(src)
with open('sportmaster.html', 'w') as file:
    file.write(src)