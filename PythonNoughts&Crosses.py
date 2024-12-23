# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:03:58 2024

@author: Michael
"""

gameBoard = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '5': ' ', '4': ' ', '1': ' ', '2': ' ', '3': ' ' }
game_keys = []

def printGame(game):
    print(game['7'] + '|' + game['8'] + '|' + game['9'])
    print('-+-+-')
    print(game['4'] + '|' + game['5'] + '|' + game['6'])
    print('-+-+-')
    print(game['1'] + '|' + game['2'] + '|' + game['3'])
    
def play():
    turn = 'X'
    count = 0
    for i in range(10):
        printGame(gameBoard)
        print("Your turn, please select a square.")
        move = input()
        if gameBoard[move]== ' ':
            gameBoard[move] = turn
            count +=1
        else:
            print("There is already a shape here, please try again.")
            continue
        if count >= 5:
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ': # across the top
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ': # across the middle
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ': # across the bottom
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ': # down the left side
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ': # down the middle
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ': # down the right side
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ': # diagonal
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ': # diagonal
                printGame(gameBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("Draw.")

        # we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'  

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in game_keys:
            gameBoard[key] = " "

        play()

if __name__ == "__main__":
    play()