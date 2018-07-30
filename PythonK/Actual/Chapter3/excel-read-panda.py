import pandas as pd

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

filename = "stat_population.xlsx"
sheet_name = "Sheet0"

book = pd.read_excel(filename, sheet_name, header=0)
book = book.sort_values(by="2016", ascending=False)

print(book)
