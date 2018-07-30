#List Comprehension
x = [y**y for y in range(5) if y % 2 == 0]
x2 = [_ for _ in range(4)]
pairs = [
    (x, y)
        for x in range(9)
        for y in range(9)
]

print('List Comprehension')
print(x)
print(x2)

#Dict Comprehension
square_Dict = { x1 : x1 * 2 for x1 in range(3)}

print('Dict Comprehension')
print(square_Dict)

#Set Comprehension
set_Comp = { s * s for s in [1, -1] }
print(set_Comp)
