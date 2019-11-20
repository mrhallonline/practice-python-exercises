# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

userString = input("Enter a word to check if it is a palindrome. ")
userString1 = userString.lower()
userString1 = userString1.replace(",", "")
userString1 = userString1.replace(" ", "")
userString2 = list(userString1)
reverseString = userString2.copy()
reverseString.reverse()

if userString2 == reverseString:
    print(userString + " is a palindrome!")
else:
    print(userString + " isn't a palindrome!")