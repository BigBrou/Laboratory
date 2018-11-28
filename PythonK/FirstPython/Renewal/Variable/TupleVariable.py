#Tuple
#Tuple is restricted to insert, update and delete
#Tuple seems like group of const variables

#Then Why python needs Tuple?

#When Change Values between variable and variable
#When return whole data in once
#When insert various datas in Dictionary

VtTupleArr = (1,2,3)

VlList = [1,2,3]
VtTupleByList = tuple(VlList)
ViIdx = 0

for VtTuple in VtTupleArr:
    print(VtTuple)
    print(VtTupleByList[ViIdx])
    ViIdx += 1
