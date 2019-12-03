import PyPDF2
import os
os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Mine\practice-python-exercises\pdfFiles')

pdfFile = open('wsu-js-cheat-sheet.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())