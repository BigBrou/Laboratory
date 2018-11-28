import re

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')

print(m)

################################

p = re.compile('[a-z]+', re.IGNORECASE)
m = p.match('Python')

print(m)

################################

p = re.compile('^python\s\w+', re.MULTILINE)
data = '''python one
life is too short
python two
you need python
python three'''

print(p.findall(data))

################################

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r'''
    &[#]
    (
        0[0-7]+
        | [0-9]+
        | x[0-9a-fA-F]+
    );
''', re.VERBOSE)

#r은 raw Data 를 말하는 것임. 백슬래시 문제 때문에 r을 앞에 붙이는 거