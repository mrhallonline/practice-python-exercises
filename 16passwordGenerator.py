# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

symbolsList = ['`', '!', '?', '$', '?', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', ':', ';', '@', '~', '#', '|', '\\', '<', ',', '>', '.', '?', '/']
alphaList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
numberList = []

def password_generator(number_of_digits):
    new_password=[]
    character_list= [symbolsList,alphaList,numberList]
    for i in range (number_of_digits):
           random_character = random.choice(alphaList)
           new_password.append(random_character)
           joined_password="".join(new_password)
    print(joined_password)


password_generator(20)




def list_maker (rawList):
    rawList.replace(" ","")
    newList= rawList.split()
    print(newList)
    
list_maker(symbolsList)