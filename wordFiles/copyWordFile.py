import docx
import os
os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Mine\practice-python-exercises\wordFiles')

def getText(filename):
    doc =docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


print(getText('demo.docx'))