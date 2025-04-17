import random
import os
clear = lambda: os.system('cls')

def rockPaperScissors():
    otherTurn = random.randrange(1, 4)
    print("Make your selection:\n 1) Rock. \n 2) Paper.\n 3) Scissors")
    Turn = input()
    
    if Turn == "1":
        if otherTurn == 1:
            print("You both picked rock Draw!")
        elif otherTurn == 2:
            print("You picked rock, other player picked paper. You lose!")
        elif otherTurn == 3:
            print("You picked rock, other player picked scissors. You win!")
        else:
            print("incorrect input, restarting.")
            clear()
            rockPaperScissors()
            
    elif Turn == "2":
        if otherTurn == 1:
            print("You picked paper, other player picked rock. You win!")
        elif otherTurn == 2:
            print("You both picked paper. Draw!")
        elif otherTurn == 3:
            print("You picked paper, other player picked scissors. You lose!")
        else:
            print("incorrect input, restarting.")
            clear()
            rockPaperScissors()
            
    elif Turn == "3":
        if otherTurn == 1:
            print("You picked scissors, other player picked rock. You lose!")
        elif otherTurn == 2:
            print("You both picked scissors, other player picked paper. You win!")
        elif otherTurn == 3:
            print("You both picked Scissors. Draw!")
        else:
            print("incorrect input, restarting.")
    
rockPaperScissors()