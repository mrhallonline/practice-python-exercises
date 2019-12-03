import openpyxl
import os

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Mine\practice-python-exercises\excel')



workbook= openpyxl.load_workbook('example.xlsx')

sheet = workbook['sheet1']
print(workbook.sheetnames)