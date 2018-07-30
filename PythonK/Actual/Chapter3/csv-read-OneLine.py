import csv, codecs
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

filename = "list-euckr.csv"
fp = codecs.open(filename, "r", "euc_kr")

reader = csv.reader(fp, delimiter=',', quotechar='"')

for cells in reader:
    print(cells)
