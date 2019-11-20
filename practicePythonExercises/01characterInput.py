import datetime
now = datetime.datetime.now()
name=input("What is your name?")
age=int(input("How old are you?"))
yearsTo100 = 100 - age
year100 = str(age + now.year)
print("Hi " + name + " you will turn 100 years old in " + year100)