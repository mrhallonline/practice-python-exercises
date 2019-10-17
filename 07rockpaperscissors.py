# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

rps = ["rock", "paper", "scissors"]
playerSelection = input("Enter rock, paper, or scissors! ")
computerSelection = random.choice(rps)

def round(player, computer):
    winner= "You win " + player + " beats " + computer
    loser=  "You lose " + computer + " beats " + player
    draw= "It's a draw " + player + " ties " + computer 
    if player==computer:
        return draw
    elif player == "rock" and computer == "scissors":
        return winner
    elif player == "rock" and computer == "paper":
        return loser
    elif player=="paper" and computer == "rock":
        return winner
    elif player=="paper" and computer == "scissors":
        return loser
    elif player=="scissors" and computer=="paper":
        return winner
    elif player=="scissors" and computer=="rock":
        return loser

print (round(playerSelection, computerSelection))

