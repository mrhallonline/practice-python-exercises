import re

# to findall occurrences
# message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line"
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneNumRegex.findall(message))

# message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line"

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search(message)
# print(mo.group())

#making groups in Regex

# message = "My number is 415-555-4242"

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search(message)
# print(mo.group(1))
# print(mo.group(2))



# Finding bats
batRegex= re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())



