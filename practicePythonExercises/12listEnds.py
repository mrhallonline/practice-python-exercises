# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# Concepts to practice
# Lists and properties of lists
# List comprehensions (maybe)
# Functions

originalList = [5, 10, 15, 20, 25]
testList = [2, 4, 6, 8, 10, 12]

def listEnds(firstList):
        endsList = [firstList[0], firstList[-1]]
        print (endsList)
        
listEnds(testList)