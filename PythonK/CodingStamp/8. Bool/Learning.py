# id returns distinct memory address
print(id(1))
print(id(1.0))

# Not use 'is' when compares price
a = -5
print(a is -5)

a = -6
print(a is -6)

#short-circuit evaluation
print(True and 'python')


print(not 1 is 1.0)
a= 10
print(not a)
