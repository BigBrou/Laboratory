import urllib.request
import urllib.parse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {'stnId': '108'}
params = urllib.parse.urlencode(values)
URL = API + "?" + params
print("URL :" , URL)

data = urllib.request.urlopen(URL).read()
text = data.decode('utf-8')
print(text)
