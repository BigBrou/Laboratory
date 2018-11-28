#requests Review
import requests
import pprint
import xml.etree.ElementTree as ET

VrRequest = requests.get('https://www.naver.com')
#pprint.pprint(VrRequest.text)

VsReqTemperature = requests.get('https://web.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000').text
#print(VsReqTemperature)
VsXMLStr = ET.fromstring(VsReqTemperature)
##for extStr in VsXMLStr.iter('data'):
##    print(extStr.find('hour').text)

import webbrowser

VsURL = 'https://www.naver.com'
#webbrowser.open(VsURL)

import sys

print(sys.argv)
