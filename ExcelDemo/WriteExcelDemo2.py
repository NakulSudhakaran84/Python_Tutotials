from openpyxl import Workbook
from openpyxl.styles import PatternFill

wb=Workbook()
wb['Sheet'].title="Report of Automation"
sh1=wb.active

data=[('Num','Name','Result'),(1,"Nakul",90),(2,"Sudhakaran",99),(3,"Java",95)]

for i in data:
    sh1.append(i)


wb.save("C:\\Users\\Nakul Sudhakaran\\Desktop\\NewExcelDemo.xlsx")

# 3EE132 Green color code E14A32 Red color code

