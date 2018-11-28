import openpyxl

filename = "stat_population.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.active
#sheet = book.worksheet[0]

for i in range(9):
    total = int(sheet[str(chr(i+66))+"1"].value)

    seoul = int(sheet[str(chr(i+66))+"2"].value)
    output = total - seoul

    sheet[str(chr(i+66)) + "21"] = output
    cell = sheet[str(chr(i+66))+"21"]
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

filenmae = "population.xlsx"
book.save(filename)
print("ok")
