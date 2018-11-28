#divmod
quotient, remainder = divmod(5, 2)
print('quotient ', quotient)
print('remainder', remainder)
print()

#진수 표현
binary = 0b110
octaldecimal = 0o100
hexadecimal  = 0xA2
print(binary, octaldecimal, hexadecimal)
print()

#long digits
a = 10000000
b = 10_000_000
print(a)
print(b)
print(a is b, end='\n\n')

#Matrix Calculate
import numpy as np

list_x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
list_y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

list_xy = list_x @ list_y
print(list_xy)
