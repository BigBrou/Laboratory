from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

import json
import os, os.path
import datetime


jsonPath = '..\RawData'
jsonFileName = '\Data.json'

if os.path.exists(jsonPath+jsonFileName):
    jsonData = json.load(open(jsonPath+jsonFileName, 'r', encoding='utf-8'))

dayList = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

visitorByDate = {}
for jsonRaw in jsonData:
    if (jsonRaw['DOCTORUID'] == ''):
        jsDoctorUid = 0
    else:
        jsDoctorUid = int(jsonRaw['DOCTORUID'][-1])

    if not (jsDoctorUid == 1):
        continue

    jsDate = jsonRaw['JSDATE']
    jsDay = datetime.datetime.strptime(jsonRaw['JSDATE'], '%Y-%m-%d').weekday()
    jsHour = int(jsonRaw['JSTIME'][0:2])
    jsHoliday = int(jsonRaw['ISHOLIDAY'])

    visitorKey = (jsDoctorUid, jsDate, jsDay, jsHour, jsHoliday)

    if visitorKey not in visitorByDate:
        visitorByDate[visitorKey] = 0
    else:
        visitorByDate[visitorKey] += 1

reArrangeByDay = []
for rowKey, rowValue in sorted(visitorByDate.items()):
    visitorByDay = [rowKey[2], rowKey[3], rowKey[4], rowValue]
    reArrangeByDay.append(visitorByDay)

for a in sorted(reArrangeByDay):
    print(a)

visitorTrain = []
visitorLabel = []

for rowKey in sorted(reArrangeByDay):
    visitorTrain.append(rowKey[0:3])
    visitorLabel.append(rowKey[3]//5 *5)
    #print(rowKey[0:3], rowKey[3])




trainData, testData, trainLabel, testLabel = \
    train_test_split(visitorTrain, visitorLabel)

clf = svm.SVC()
clf.fit(trainData, trainLabel)

pre = clf.predict(testData)

ac_score = metrics.accuracy_score(testLabel, pre)
print(ac_score)















