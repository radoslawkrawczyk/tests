from datetime import datetime
from aaa.names import names
import xlsxwriter
from aaa.akcje_dalej import result1
from aaa.akcje_na_elementach import result2


workbook = xlsxwriter.Workbook("../aaa/Excel.xlsx")
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 'true', 'font_color': '008000'})

number = 1
time_now = datetime.now().isoformat()

worksheet.set_column(0, 0, 11)
worksheet.set_column(1, 1, 8)
worksheet.set_column(2, 2, 18)
worksheet.set_column(3, 3, 30)

worksheet.write("A1", "Date", bold)
worksheet.write("B1", "Number", bold)
worksheet.write("C1", "Test name", bold)
worksheet.write("D1", "Result", bold)

expenses = (
    [time_now[0:10], number, names[0], result1],
    ["", number + 1, names[1], result2]
)

row = 2
col = 0

for date, number, names, result in expenses:
    worksheet.write(row, col, date)
    worksheet.write(row, col + 1, number)
    worksheet.write(row, col + 2, names)
    worksheet.write(row, col + 3, result)

row += 1

print("-Plik wygenerowano")
workbook.close()