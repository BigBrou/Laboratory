import requests
from bs4 import BeautifulSoup

#VlSoup = BeautifulSoup('<html> LolliPop </html>', 'html.parser')

VsURL = requests.get('https://www.naver.com').text
VlSoup = BeautifulSoup(VsURL, 'html.parser')
print(VlSoup.title)
