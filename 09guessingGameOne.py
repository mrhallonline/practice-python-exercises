# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random
computerNumber = random.randint(1, 9)

print (computerNumber)
userNumber = int(input("guess the number between 1 and 9 "))
userNumber2 = str(userNumber)

if userNumber == computerNumber:
    print("You have picked the correct number")
elif userNumber > computerNumber:
    print(str(userNumber) + " is too large!")
elif userNumber < computerNumber:
    print(str(userNumber) + " is too small!")