# 3배수에 해당하는 내용 3배 한 값을 을 넣어라
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


result = [y * 3 for y in list if y % 3 == 0]
print(result)

def sum(a, b):
    return a + b

print(sum(3, 5))

'''
def 함수이름(*매개변수):
    <수행할 문장>
'''

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(1, 2, 3))

#kwargs 베리베리 임포턴트
# keyword arguemnts
def func(**kwargs):
    print(kwargs)

func(a=1)
func(name='foo', age='3')

#dictionary 형태로 저장을 해준다.
def func(*args, **kwargs):
    print(type(args))
    print(args)
    print(kwargs)
func(1, 2, 3, name='foot', age = '4')



#global
a = 1
def vartest():
    global a
    a = a+1
vartest()
print(a)

#lambda
sum = lambda x,y : x + y
print(sum(3, 4))
