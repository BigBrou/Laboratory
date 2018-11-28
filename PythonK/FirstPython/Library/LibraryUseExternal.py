# with cmd command
# pip install LibraryName
# pip deinstall LibraryName
# pip show LibraryName

from PIL import Image

VimImage = Image.open('C:\\Desert.jpg')
r, g, b = VimImage.split()

VimImageColor = Image.merge('RGB', (b, r, g))
#VimImageColor.show()

VimImageBlackWhite = VimImage.convert('1')
#VimImageBlackWhite.show()

VimImageGray = VimImage.convert('L')
#VimImageGray.transpose(Image.ROTATE_90).show()


#################################################
import requests
import pprint
import xml.etree.ElementTree as ET

VRequest = requests.get('https://www.naver.com')
#pprint.pprint(VRequest.text)

VsUrl = 'https://web.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000'
VReqWeather = requests.get(VsUrl).text
#pprint.pprint(VReqWeather)
VsXMLStr = ET.fromstring(VReqWeather)
for tag in VsXMLStr.iter('data'):
    print(tag.find('hour').text + '/'+ tag.find('temp').text)
