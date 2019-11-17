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

# def animal_crackers(text):
#     splitString = text.split()
#     if (splitString[0][0]==splitString[1][0]):
#         return True
#     else:
#         return False
    
# animal_crackers('Levelheaded Llama')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# def makes_twenty(n1,n2):
#     if (n1==20 or n2==20 or (n1+n2)==20):
#         return True
#     else:
#         return False


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

# x = ('apple')
# y = enumerate(x)

# return (list(y))

# def old_macdonald(name):
#     newString =''
#     for x, c in enumerate(name):
#         if (x==0):
#             newString += c.upper()
#         elif (x==3):
#             newString += c.upper()
#         elif (x!=0 or x!=3):
#             newString += c
#     return(newString)
# old_macdonald('macdonald')


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

# def masteryoda(text):
#     newSentence = []
#     text.split()
#     for x, c in enumerate(text):
#         if x == -1:
#             newSentence.insert(0, c)
#         elif x == 0:
#             newSentence.insert(-1, c)
#         else:
#             newSentence.insert(1, c)
#     newerSentence = newSentence.join()
#     print(newerSentence)

# masteryoda('yesterday is today')


# def masteryoda(text):
#     newerSentence = []
#     newSentence = text.split()
#     newerSentence.insert(0, newSentence[-1])
#     newerSentence.insert(-1, newSentence[0])
    
#     print(newerSentence)

# masteryoda('yesterday is today')


# def masteryoda(text):
#     newerSentence = []
#     newSentence = text.split()
#     newSentence.append(newSentence[0])
#     print(newSentence)
#     newSentence[0]=newSentence[-2]
#     print(newSentence)
#     newSentence[-2]=newSentence[-1]
#     print(newSentence)
#     newSentence.pop()
#     print(newSentence)
# masteryoda('yesterday is today')


# def masteryoda(text):
#     newSentence = text.split()
#     newSentence.append(newSentence[0])
#     newSentence[0]=newSentence[-2]
#     newSentence[-2]=newSentence[-1]
#     newSentence.pop()
# masteryoda('yesterday is today')


# def masteryoda(text):
#     text = text.split()
#     text.append(text[0])
#     text[0]=text[-2]
#     text[-2]=text[-1]
#     text.pop()
#     newSentence = " ".join(text)
# masteryoda('yesterday is today')


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

# def almost_there(n):
#     if (n in range(90,110)):
#         return True
#     elif (n in range(190, 210)):
#         return True
#     else:
#         return False
    
# def almost_there(n):
#     if (abs(100 -n) < 10) or (abs(200-n)<10):
#         return True
#     else:
#         return False 
    
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

def has_33(nums):
    for index in range (len(nums)-1):
        if (nums[index] == nums[index+1]):
           return True 
        else:
            return False

def has_33(nums):
     for i in range (len(nums)-1):
        if (nums[i] == 3 and nums[i+1]==3 ):
            signal=True
        else:
            signal=False
     return signal