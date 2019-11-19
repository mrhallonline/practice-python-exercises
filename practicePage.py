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
    
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# def has_33(nums):
#     for index in range (len(nums)-1):
#         if (nums[index] == nums[index+1]):
#            return True 
#         else:
#             return False

# def has_33(nums):
#      for i in range (len(nums)-1):
#         if (nums[i] == 3 and nums[i+1]==3 ):
#             signal=True
#         else:
#             signal=False
#      return signal



# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(text):
#     tripleWord=""
#     for letter in range(len(text)):
#         tripleWord = (text[letter]*3)
#     print(tripleWord)

# paper_doll('Hello')

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

# def blackjack(a,b,c):
#     roundOne = a+b+c
#     if (roundOne<=21):
#         return roundOne
#     elif (roundOne > 21 and 11 in blackjack):
#             roundTwo = roundOne-10
#             if (roundTwo > 21):
#                 return "Bust"
#             else:
#                 return roundTwo
#     else:
#         return "Bust" 
    
# def blackjack(a,b,c):
#     thisTup = (a,b,c)
#     roundOne = a+b+c
#     x=thisTup.count(11)
#     if (roundOne<=21):
#         return (roundOne)
#     elif (roundOne > 21 and x > 0):
#             roundTwo = roundOne-10
#             if (roundTwo > 21):
#                 return ("Bust")
#             else:
#                 return (roundTwo)
#     else:
#         return ("Bust")

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

# def summer_69(arr):
#     sumList = sum(arr)
#     sixExist = False
#     sixCount = arr.count(6)
#     if sumList = 0
#     if (sixCount>0):
#         sixIndex = arr.index(6)
#         nineIndex = arr.index(9)
#         del arr[sixIndex:nineIndex+1]
#     sumList = sum(arr)
#     return sumList
# summer_69([4, 5, 6, 7, 8, 9])

# def summer_69(arr):
#     sumList = sum(arr)
#     sixCount = arr.count(6)
#     if (sumList == 0):
#         return 0
#     if (sixCount>0):
#         sixIndex = arr.index(6)
#         nineIndex = arr.index(9)
#         del arr[sixIndex:nineIndex+1]
#     sumList = sum(arr)
#     return sumList
# summer_69([4, 5, 6, 7, 8, 9])  

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False
 
# def spy_game(nums):
#     spyList=[]
#     for num in nums:
#         if (num ==0):
#            spyList.append(num)
#         if (num ==7):
#            spyList.append(num)
#     print(spyList) 
# spy_game([1,7,2,0,4,5,0]) 

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

# def count_primes(num):
#     for i in range(2,num):
#         if (num%i):
            
            


