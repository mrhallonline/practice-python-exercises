# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random
guesses = 0
computerNumber = random.randint(1, 9)
def computerChoose():
    global computerNumber
    computerNumber = str(random.randint(1, 9))

def gameSetup():
    global userNumber
    userNumber = input("Guess a number between 1 and 9. Type exit to quit :")
    global guesses
    guesses += 1
    gamePlay()

def gamePlay():
    while userNumber != "exit":
        if int(userNumber) == int(computerNumber):
            print("You guessed correct in " +str(guesses)+ " guesses")
            computerChoose()
            gameSetup()
        elif int(userNumber) > int(computerNumber):
            print(userNumber + " is too large!")
            gameSetup()
        elif int(userNumber) < int(computerNumber):
            print(userNumber + " is too small!")
            gameSetup()
gameSetup()
