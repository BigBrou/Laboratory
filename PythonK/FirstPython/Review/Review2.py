#Variable

#Variable string, float
AText = 'Text Variable'
AIndex = 1234.44
print(AText, AIndex, AText * 2)

#Use import
from datetime import datetime
hour = datetime.now().hour
print(hour)

#procedure, if, array
Position = ['School', 'Military Base', 'Pochinky']

def GetLost(landing):
    for land in Position:
        if (land == landing):
            result = 'Hell Gate'
            break
        else:
            result = 'Can not parming'
    return result, landing

print(GetLost('Pochinky'))

# input
#input('Write in this Line : ')


#list add remove
Position.append('None')
print(Position)
