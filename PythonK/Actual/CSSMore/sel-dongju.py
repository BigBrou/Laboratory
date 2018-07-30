from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), "utf-8")


url = "https://ko.wikisource.org/wiki/%ED%95%98%EB%8A%98%EA%B3%BC_%EB%B0%94%EB%9E%8C%EA%B3%BC_%EB%B3%84%EA%B3%BC_%EC%8B%9C"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

#mw-content-text > div > ul > li a
a_list = soup.select("last-child")

for a in a_list:
    name = a.string
    print("-", name)
