import re

p = re.compile('^Life', re.IGNORECASE)
m = p.search('life is too short')

print(m)

# ^ 와 \A 의 차이는 라인에 따라 인식을 하느냐 안하느냐의 차이
# $ 와 \Z 의 차이는 라인에 따라 인식을 하느냐 안하느냐의 차이
# \b Word boundary 이다. whitespace에 의해 구분이 된다.

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

#####################################################

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m.group())

#####################################################

p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')
m = p.search('park  010-33333-444444')
print(m)

p = re.compile(r'(\w+)\s+(\d+[-]\d+[-]\d+)')
m = p.search('park  010-33333-444444')
print(m.group(0))
print(m.group(1))
print(m.group(2))

p = re.compile(r'(\b\w+)\s+\1')
m = p.search('the the the').group()
print(m)

################################
p = re.compile(r'(?P<names>\w+)\s+((\d{3})[-](\d{4})[-](\d{4}))')
m = p.search('park  010-2054-9870')
print(m.group('names'))