
import re, pyperclip

#  create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?                               # area code (optional)
(\s|-)                         # separator     
\d\d\d                               # first 3 digits
-                               # separator
\d\d\d\d                              # last 4 digits
(((ext(\.)?\s)|x)                            # extensionwords (optional)
(\d{2,5}))?                       # extension digits(optional)
)
 ''', re.VERBOSE)

#  create a regex for email addresses

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+                                   # name part
@                                   # at symbol 
[a-zA-Z0-9_.+]+                                   # domain part                  
''',re.VERBOSE)


#  get the text off the clipboard
text = pyperclip.paste()

#  extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
# print(allPhoneNumbers)
# print(extractedEmail)

# TODO copy the extracted email/phone to the clipboard 
results = '\n'.join(allPhoneNumbers) +'\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)