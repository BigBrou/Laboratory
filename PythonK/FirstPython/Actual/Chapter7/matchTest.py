import re

p = re.compile('[a-z]+')
m = p.match('string goes here')

if m:
    print('match', m.group())
else:
    print('^match')

m = p.search('3 python')
print(m)

result = p.findall("life if too short")
print(result)

result = p.finditer("life is too short")
print(result)
for r in result:
    print(r)

m = p.match('delphi is sucks')
print(m.group())
print(m.start())
print(m.end())
print(m.span())