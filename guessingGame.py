import random
playerGuess = 0
round = 1

    
rightNumber = random.randint(1, 100)
playerGuess= input("Choose a number.")
while (playerGuess != rightNumber):
    if (playerGuess < 1 or playerGuess > 100):
        print("Out of Bounds")
        chooseNumber()
    if (round ==1 and playerGuess in range(rightNumber-10,rightNumber+10) ):
        print("WARM!")
        chooseNumber()

         
def chooseNumber():
    playerGuess= input("Choose a number.")