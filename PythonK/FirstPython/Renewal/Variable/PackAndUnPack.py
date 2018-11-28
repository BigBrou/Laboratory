#Packing
#하나의 변수에 여러 개의 값을 넣는 것

#Unpacking
#패킹된 변수에서 여려 개의 값을 꺼내오는 것

(a, b) = (1, 2) # == a, b = 1, 2
c = (3, 4)

(d, e) = c      # This is Unpacking
f = (d, e)      # This is Packing

VlList = [1,2,3,4,5]
VlDictionary = {
    'a' : 16,
    'b' : 17,
    'c' : 18,
    'd' : 19,
    'e' : 20
}

for VtTuple in enumerate(VlList):
    print(VtTuple[0], VtTuple[1])

try:
    for VtTuple in VlDictionary.items():
        print('{}, {}'.format(VtTuple[0], VtTuple[1])
except Exception as Ex:
    print('Exception Occured', Ex)
