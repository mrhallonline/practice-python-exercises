# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

symbolsList = [ '!', '?', '$', '?', '%', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', ':', ';', '@', '~', '#', '|', '<', ',', '>', '.', '?', '/']
alphaList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

def password_generator(number_of_digits):
    number_of_digits = int(input("How many characters do you want in the password?: "))
    new_password=[]
    for i in range (number_of_digits):
           selector_seed = random.randint(0,6)
           numberList = random.randint(0,9)
           symbols = random.choice(symbolsList)
           alpha = random.choice(alphaList)
           random_character = (alpha, alpha, alpha, alpha, symbols , alpha , numberList)
           new_password.append(random_character[selector_seed])
    new_password = ''.join([str(char) for char in new_password])
    print(new_password)
    
password_generator(25)