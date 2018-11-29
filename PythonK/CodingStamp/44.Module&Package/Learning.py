#Package Import (both same)

from urllib import request as req
import urllib.request as req

url = 'http://google.com'
response = req.urlopen(url)
print(response.status)
