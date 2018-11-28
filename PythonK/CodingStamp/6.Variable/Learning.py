#Assign Variable
x, y, z = 10, 20, 30
a = b = c = 40

print(x, y, z)
print(a, b, c)

#Swap Variable
x, y = y, x
print(x, y, z)

#Delete Variable
del x, y, z

#Assign null nullType Data
x = None
print(x, type(x))

#Assign & Calculate at Once
num = 90

num += 10
num *= 20
num /= 5
num //= 2
print(num)

#
import sys
print(sys.getrefcount(10000))
a = 10000
print(sys.getrefcount(10000))
print(sys.getrefcount(a))
