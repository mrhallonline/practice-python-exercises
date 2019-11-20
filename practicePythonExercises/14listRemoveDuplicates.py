# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_duplicates(firstList):
    firstList=set(firstList)
    firstList =list(firstList)
    return firstList

def remove_duplicates2(firstList):
    secondList =[]
    for item in firstList:
        if item not in secondList:
            secondList.append(item)        
    print(secondList)
           

names = ["Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara","Michele","Robin","Sara",]
remove_duplicates2(names)

    