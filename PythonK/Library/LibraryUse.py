#Import Library
##Import datetime of datetime only
from datetime import date, timedelta

VsDate = date.today()
print(VsDate.strftime('%y/%m/%d'))
VtOneweek = timedelta(days= 7)
VsDate = VsDate + VtOneweek
print(VsDate.strftime('%y/%m/%d'))

####################################
import zipfile

VsCompressFileName = zipfile.ZipFile('C:\\PythonTest.zip', 'w')
VsCompressFileName.write('C:\\cdx.ini', 'cdx')
VsCompressFileName.close()

VsFileConfirm = zipfile.ZipFile('C:\\PythonTest.Zip')
print(VsFileConfirm.namelist())
VsFileConfirm.extractall()
VsFileConfirm.close()

####################################

#File Use
VfFile = open('C:\\Test.txt', 'a')
VfFile.write('C#')
VfFile.flush()

VfFile = open('C:\\Test.txt', 'r+')
VfFile.write('r+\n')
VfFile.seek(0)                       #Move Cursor to Start
print(VfFile.read())
VfFile.close()

with open('C:\\Test.txt', 'r+') as VfFileWith:
    VfFileWith.write('No Need to Close \\n')
