# The Challenge:

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!


import random
# playerGuess = 0
round = 1
def chooseNumber():
    playerGuess= int(input("Choose a number."))
    
def playRound():
    playerGuess= int(input("Choose a number."))
    while (playerGuess != rightNumber):
        if (playerGuess < 1 or playerGuess > 100):
            print("Out of Bounds!")
            print(playerGuess)
            print(rightNumber)
            round += 1
            playerGuess= int(input("Choose a number."))
        elif (round ==1 and playerGuess in range(rightNumber-10,rightNumber+10) ):
            print("WARM!")
            print(playerGuess)
            print(rightNumber)
            playerGuess= int(input("Choose a number."))
        elif (round == 1 and playerGuess < rightNumber-10 or playerGuess > rightNumber+10):
            print("Cold!")
            playerGuess= int(input("Choose a number."))
        else:
            print("wrong")
            print(playerGuess)
            print(rightNumber)
            playerGuess= int(input("Choose a number."))
    print("You got the right answer!")
         
rightNumber = random.randint(1, 100)
playRound()