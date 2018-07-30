dic = {}
dic = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(dic)

a = {'a' : [1, 2, 3]}
print(a)

a[2] = 'b'  # Key 와 Value를 넣는 것이다
print(a)

#del a['a'] # Key를 입력하면 된다.
#print(a)

print(a.keys())
print(a.values())

print(list(a.keys()))
print(list(a.values()))

print(a.items())

a.clear()
print(a)


#Quiz 1
dic = {
    'name'  : '홍길동',
    'birth' : 1128,
    'age'   : 30
}

#Quiz 2
a = dict()
print(a)

#Quiz 3
a = {'A':90, 'B':80, 'C':70}
print(a.get('D', 90))
del a['B']
print(a)

#Quiz 5
print(list(a.items()))