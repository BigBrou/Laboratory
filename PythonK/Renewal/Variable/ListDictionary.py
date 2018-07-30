# List
# List Value
# List insert, delete, update

VlListInt = [1,2,3,4,5]
VlListStr = ['1','2','3','4','5']

VlListInt.append(6)
VlListInt.remove(6)
VlListInt.pop(2)
VlListInt.remove(VlListInt[2])
del(VlListInt[0])
VlListInt = VlListInt + [1]
3 in VlListInt
print(VlListInt)

# Dictionary
# Dictionary Key, Value
# Dictionary insert, delete, update

VdDicArr = {
    '1' : 10,
    '2' : 20,
    '3' : 30,
    '4' : 40,
    '5' : 50
}
VdDicArr['6'] = 60
VdDicArr['3'] = 33
del(VdDicArr['2'] )
VdDicArr.pop('3')

for Dic in VdDicArr.keys():
    print(Dic)

for DicValue in VdDicArr.values():
    print(DicValue)

for DicKey, DicValue in VdDicArr.items():
    print(DicKey, DicValue)

print(VdDicArr)
