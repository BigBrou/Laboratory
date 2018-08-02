import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_json('..\RawData\Data.json')


#dataFrame['DOCTORUID'] = pd.factorize(dataFrame['DOCTORUID'])
dataFrame['DATE']     = pd.to_datetime(dataFrame['JSDATE'])
dataFrame['JSDATE']   = pd.to_datetime(dataFrame['JSDATE'])
dataFrame['DAY']      = dataFrame['JSDATE'].dt.weekday
dataFrame['UNIXDATE'] = dataFrame['JSDATE'].view('int64')
dataFrame['JSDATE']   = pd.to_numeric(dataFrame['JSDATE'])
dataFrame['JSHOUR'] = pd.to_numeric(dataFrame['JSTIME'].str.slice(0, 2))
dataFrame['JSTIME']   = pd.to_timedelta(dataFrame['JSTIME'])



#re = dataFrame.corr(method='pearson')
#print(re)
datadata = dataFrame.head(10)

plt.plot(datadata['JSHOUR'], datadata['JSHOUR'])


plt.show()