import codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

filename = 'list-euckr.csv'
csv = codecs.open(filename, 'r', "euc_kr").read()

data = []
rows = csv.split("\r\n")
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)

for c in data:
    print(c[0], c[1], c[2])
