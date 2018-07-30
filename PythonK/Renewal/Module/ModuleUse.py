#Use Module by import

#math
import math

ViPi = math.pi
ViRadian = 10
ViDiameter = ViRadian * 2 * ViPi

print(ViDiameter)

#random
import random

candidates = ['Scissors', 'Rock', 'Paper']

for select in range(3):
    selected = random.choice(candidates)
    print(selected)

#urllib
'''
import urllib

def get_web(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')

    return decoded

content = get_web("http://www.naver.com")
print(content)
'''
