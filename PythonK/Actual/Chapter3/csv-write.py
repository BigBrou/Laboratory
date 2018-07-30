import csv, codecs

with codecs.open("test.csv", "w", "euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "NAME", "PRICE"])
    writer.writerow(["1006", "SD CARD", "30000"])
    writer.writerow(["1007", "KEYBOARD", "20000"])
    writer.writerow(["1008", "MOUSE", "15000"])
