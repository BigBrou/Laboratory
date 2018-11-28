text = 'hello'
print('Text Value : '+ text)
print('Text Point Where L Is :' + str(text.count('l')))

print(44 < 66)

Alphabet = ['ABC', 'DEF', 'EFG']
for count in Alphabet:
    print(count)
Alphabet.append('jkl')
for count in Alphabet:
    print(Alphabet)

Test = {'Test1':95, 'Test2':94, 'Test3':93}
print(Test['Test1'])

#Text = {44:'ka', 55:'yang', 66:'mi'}
#for count in Text:
#    print(Text.key())

tuple_tuple = ('plane', 3, 'Notorious')
tuple_tuple2 = ('car', 2, 'gkgk')

print(tuple_tuple)
Diction = {}
Diction[tuple_tuple] = 'NiceRider'
Diction[tuple_tuple2] = 'gkgkHaller'

print(Diction)

CrimeCity = set('garibongdong')
print(CrimeCity)

JoshunJok = ['jangchen', 'yangtae', 'dokki']
CrimeCity = set(JoshunJok)
print(CrimeCity)

CrimeCity.update(['madongsuk'])
print(CrimeCity)

ACrimePeople = 1
if (ACrimePeople > 3):
    ADay = 'Develop'
elif (ACrimePeople > 2):
    ADay = 'JangChen'
else:
    ADay = 'MaDongSuk'
print(ADay)
# This is the end of Value

def procedure ():
    print('This is the procedure')
    print('Remind of Python')

procedure()

def Function (AIdx):
    if (AIdx > 5):
        print('Case Function of AIdx')
    else:
        print('Need to know this is occurate in here')

Function(5)

try:
    Function('Test')
except Exception as e:
    print(e.args)
