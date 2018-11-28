#Quiz1
def is_odd(a):
    if a <= 0: return

    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')

is_odd(356)

#Quiz2
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_many(1, 3, 5, 7, 9))

#Quiz3
def multiflication(x):
    if not ((x>=2) & (x <= 9)): return
    for i in range(1,10):
        print(x * i, end = ' ')

multiflication(2)
print(end='\n')

#Quiz4
def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-2) + fibo(n - 1)

print(fibo(9))

#Quiz5
myfunc = lambda list: [x for x in list if x > 5]
print(myfunc([1, 2, 3, 5, 6, 7, 8, 9]))
