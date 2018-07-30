a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'list', 'is']
e = [1, 2, ['list', 'are']]
print(e)

print(e[2])
print(e[2][0])
print(e[0:])
print(e[:2])
print(e[0]+e[1])

a = [1, 2, 3]
print(a * 3)

#숫자를 문자로
b = str(a[1]) + 'hi'
print(b)

a = [1, 2, 3]
print(a[2])


print ('--------------------')

a = [1, 2, 3]
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
print(a)

a = [1, 2, 3]
a[1] = ['a', 'b', 'c']
print(a)

del(a[2])
del a[1]
print(a)

a.append(4)
a.append('hil')
print(a)
#a.sort() # This takes an error cause of different type
#a.reverse()

aster = [1, 2, 3]
aster.insert(0, 4)
aster.insert(3, 5)
print(aster)

aster.remove(2) #값을 제거하는 방법
print(aster)

astr = [1, 2, 3]
astr.pop(1) #위치 상의 값을 제거
print(astr)
print(astr.count(2))

print('====================')

#list extend
a = [1, 2, 3]
b = ['a', 'b']
a.extend(b)
print(a)


####
#Quiz 1
a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python']
print (a[4] , a[2])

#Quiz 2
list = ['Life', 'is', 'too', 'short']
result = " ".join(list)
print(result)

#Quiz 3
a = [1, 2, 3]
print(len(a))

#Quiz 4
a = [1, 2, 3]
b = [4, 5]
#a.append(b)
#a.extend(b)
print(a)

#Quiz 5
a = [1, 3, 5, 4, 2]
a.sort()
print(a)

#Quiz 6
a = [1, 2, 3, 4, 5]
a.pop(1)
a.remove(4)
print(a)