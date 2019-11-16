# def my_func(t='string'):
#     newstring=''
#     for count, element in enumerate(t):
#         if count%2==0:
#             newstring += element.lower()
#         else:
#             newstring += element.upper()
#     return newstring

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

# def lesser_of_two_evens(a,b):
#     if (a%2==0 and b%2==0):
#         if (a>b):
#             return b
#         else:
#             return a
#     else:
#         if (a>b):
#             return a
#         else:
#             return b
        
# lesser_of_two_evens(2,4)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    splitString = text.split()
    if (splitString[0][0]==splitString[1][0]):
        return True
    else:
        return False
    
animal_crackers('Levelheaded Llama')