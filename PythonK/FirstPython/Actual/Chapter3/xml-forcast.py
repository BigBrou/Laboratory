from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdIn=108"
savename = "forecast.xml"

#if not os.path.exists(savename):
req.urlretrieve(url, savename)

xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

info = {}
for location in soup.find_all("location"):
    name = location.find_next("city").string
    weather = location.find("wf").stringlll
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print(" -", name)
