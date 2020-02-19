# -*- coding: utf-8 -*-
from datetime import datetime
from names import names
import xlsxwriter
from testingClass import TestingClass

workbook = xlsxwriter.Workbook("./Excel.xlsx")
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

testingClass = TestingClass()

testResults = testingClass.runTests()

fixedExpenses = [];

counter = 1
nameCounter = 0

for testResult in testResults:
    fixedExpenses.append([
        time_now[0:10], counter, names[nameCounter], testResult
    ])
    counter+=1
    nameCounter+=1


row = 2
col = 0

for date, number, names, result in fixedExpenses:
    color = lambda xx: 'red' if xx == False else 'green'
    cell_format = workbook.add_format({'bg_color': color(result)})

    worksheet.write(row, col, date)
    worksheet.write(row, col + 1, number)
    worksheet.write(row, col + 2, names)
    worksheet.write(row, col + 3, "passed" if result == True else "failed", cell_format)
    row += 1

print("-Plik wygenerowano")
workbook.close()
