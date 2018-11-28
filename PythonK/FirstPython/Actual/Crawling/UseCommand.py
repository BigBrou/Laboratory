import sys
import io
import urllib.request as req
import urllib.parse as parse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), "utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), "utf-8")

if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'stdIn':regionNumber}
params = parse.urlencode(values)
url = API + "?" + params
print("url :", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
