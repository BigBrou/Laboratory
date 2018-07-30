from sklearn import svm, metrics

import json
import os, os.path
import datetime
import copy

#Load JsonData
jsonPath = '..\RawData'
jsonFileName = '\Data.json'

if os.path.exists(jsonPath+jsonFileName):
    jsonData = json.load(open(jsonPath+jsonFileName, 'r', encoding='utf-8'))

#Classify By Hour
hourSection = []
for hour in range(0, 24):
    if (hour < 10):
        hourSection.append('0'+str(hour))
    else:
        hourSection.append(str(hour))
print(hourSection)

#Initalize Zero List
visitorCount = ['', [0 for _ in range(0, 24)], False]
dayList = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']
print(visitorCount)

#Make Hour Dict
visitorByDate = {}
for jsonRaw in jsonData:
    visitorKey = (jsonRaw['JSDATE'], jsonRaw['DOCTORUID'])
    if visitorKey not in visitorByDate:
        visitorByDate[visitorKey] = copy.deepcopy(visitorCount)
        visitorByDate.get(visitorKey)[0] = datetime.date(int(visitorKey[0][:4]), int(visitorKey[0][5:7]), int(visitorKey[0][8:10])).weekday()
        visitorByDate.get(visitorKey)[2] = (jsonRaw['ISHOLIDAY'] == '1')

    jsHour = int(jsonRaw['JSTIME'][0:2]) % 24
    visitorByDate.get(visitorKey)[1][jsHour] += 1

'''for rowKey, rowValue in sorted(visitorByDate.items(), key=lambda x: x[0]):
    print(rowKey, rowValue)'''


#Extract Doctor's Date
doctorsList = {}
for rowKey, rowValue in sorted(visitorByDate.items(), key=lambda x: x[0]):
    if (rowKey[1] == 'doctor1') and (rowValue[0] == 3):
        doctorsList[rowKey[0]] = rowValue
        print(rowKey[0], doctorsList[rowKey[0]])

trainData  = []
trainLabel = []
testData   = []
testLabel  = []

idx = 0
'''
for dataValue in doctorsList.values():
    idx += 1
    if (idx % 5 == 0):
        testData.append([dataValue[0]])
        testLabel.append(dataValue[2][9:19])
    else:
        trainData.append([dataValue[0]])
        trainLabel.append(dataValue[2][9:19])

#Data Learning
clf = svm.SVC()
clf.fit(trainData, trainLabel)
pre = clf.predict(testData)

ac_score = metrics.accuracy_score(testLabel, pre)
print(ac_score)

'''

for dataValue in doctorsList.values():
    idx += 1
    if (idx % 5 == 0):
        testData.append([dataValue[0]])
        testLabel.append(dataValue[1][15:16])
    else:
        trainData.append([dataValue[0]])
        trainLabel.append(dataValue[1][15:16])

clf = svm.SVC()
clf.fit(trainData, trainLabel)
pre = clf.predict(testData)

ac_score = metrics.accuracy_score(testLabel, pre)
print(ac_score)






















