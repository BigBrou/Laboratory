#currying

from functools import partial

def double(x):
    return x * 2

xs = [1, 2, 3, 4]
double_xs = [double(x) for x in xs]
double_xs2 = list(map(double, xs))
doubler = partial(double, 2)

print(double_xs)
print(double_xs2)
print(doubler())

#enumerate
documents = 'i feel it comming'

for i in range(len(documents)):
    document = documents[i]
# not Pythonish

#when we just need index
for i, _ in enumerate(documents):
    print(i)

#zip & argment unpacking
#zip makes list to tuple list
list1 = [1, 2, 3]  # key
list2 = [4, 5, 6]  # value
list3 = list(zip(list1, list2))
print(list3)
list4, list5 = zip(*list3)
print(list4)
print(list5)

#args & kwargs
def magic(*args, **kwargs):
    print('unnamed args : ', args)
    print('keyword args : ', kwargs)

magic(1, 2, 3 ,key ="word", key2 = "word2")
