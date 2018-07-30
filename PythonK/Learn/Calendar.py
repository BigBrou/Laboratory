text = 'hello'
print(text.count('l'))

print(46 < 66)

Alphabet = ['abc', 'def', 44]
for count in Alphabet:
	print(count)
Alphabet.append('jkl')
for count in Alphabet:
	print(count)
Alphabet.remove(44)
for count in Alphabet:
	print(count)

Alphabet.sort()
for count in Alphabet:
	print(count)


Test = {'Test1': 96, 'Test2': 97, 'Test3': 99}
print(Test['Test1'])

print(Test.keys())
print(Test.values())

tuple_sample = ('apple', 3, 90.4)
print(tuple_sample)


print('=======================')
diary = {}
key = ('kanatara', 'kangster')
diary[key] = '70kg'
print(diary)
print('=======================')
print('\n')

print('=======================')
candy = set('delicious')
print(candy)

flavor = ['hot', 'sweet', 'wet']
candy = set(flavor)
print(candy)
candy.update(['spicy'])
print(candy)

print(flavor)


print('\n')
print('\n')
print('\n')
ATeenMax = 18
if (ATeenMax < 20):
	ACount = 3;
	for AIdx in range(3):
		print('Oh Adult')
	while (ACount <= 6):
		print('gonna be Friend')
		ACount += 1
elif (ATeenMax < 16) | (ATeenMax == 18):
	print('um not Adult')
else:
	print('What a Baby Go Home')

def procedure ():
	print('procedure test 1')
	print('procedure test 2')

procedure ()



def GetArea(radius):
	result = radius * radius * 3.14
	return result

CircleArea = GetArea(3)
print(CircleArea)

print(dir())


try:
	GetArea('324')
except Exception as E:
	print(E.args)k
