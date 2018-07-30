list = [1, 2, 3, 4, 5]

list.append(6)
print(list)

list.remove(6)
print(list)

del(list[4])
print(list)

for listIndex in list:
    print(listIndex)

for AIdx in [6,7,8,9,0]:
    print(AIdx)

for AIdx in range(3):
    print(AIdx)

for AIdx in range(0, 4):
    print('range Test : ' , AIdx)

for AIdx in range(len(list)):
    print(AIdx)

#New Object enumerate
for AIdx, value in enumerate(list):
    print('{}, {}'.format(AIdx, value))
