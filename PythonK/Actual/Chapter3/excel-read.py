import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

filename = "stat_population.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]

data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[9].value
    ])

data = sorted(data, key=lambda x: x[1])

for i, a in enumerate(data):
    if(i >= 5): break
    print(i+1, a[0], a[1])
