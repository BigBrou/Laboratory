from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), "utf-8")

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

title = soup.find("title").string
wf = soup.find("wf").string

print(title)
print(wf)
