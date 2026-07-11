# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:55:36 2026

@author: MBark
"""

""" To Do:
- set invalid answer input to re-run the question function
- finsh questions 2-4 
- convert score to string in questions
- total display with variable messaging for the end   
    """
import time
import os

clear = lambda: os.system('cls')
Options = ("A", "B", "C", "D")
score = 0
questionCount = 0


questionOne = "Which class is a platypus?"
questionOneAnswers = {"A" : "Fish", "B" : "Bird", "C" : "Mammal", "D" : "Reptile"}

questionTwo = "Which is the capital of The United Kingdom"
questionTwoAnswers = {"A" : "London", "B" : "Moscow", "C" : "Tokyo", "D" : "New York"}

questionThree = "Which dish includes eggs as a major ingrediant "
questionThreeAnswers = {"A" : "Carbonara", "B" : "Arabiata", "C" : "Lasagna", "D" : "Cacio e Pepe"}

questionFour = "Which is the square root of 49"
questionFourAnswers = {"A" : "6", "B" : "7", "C" : "8", "D" : "9"}

questionFive = "What is the name for romanized Mandarin"
questionFiveAnswers = {"A" : "Kanji", "B" : "Hanwu", "C" : "Hangul", "D" : "Pinyin"}
    

def runQuiz():
    
    print ("Welcome to the quiz!")
    time.sleep(2)
    print ("Please enter A, B, C or D when prompted to answer.")
    time.sleep(5)
    clear()
    for q in range(4):
        question(q)
    
    
def question(questionNum):
    global score
    
    if questionNum == 0:
        print ("Question 1!")
        time.sleep(1)
        print (questionOne)
        for i in questionOneAnswers:            
            print (i + ": " + questionOneAnswers[i])
            time.sleep(1)
        answerOne = input("Please enter your choice.").upper()
        if answerOne not in Options:
            answerOne = input("Invalid choice, please try again.").upper()
        else:
            if answerOne == "C":
                score += 1
                print(score)
                print ("Correct! Current score: " + str(score) + "/5")
            else:
                print("Incorrect! Current score: " + str(score) + "/5")
                
    elif questionNum == 1:
        print ("Question 2!")
        time.sleep(1)
        print (questionTwo)
        for i in questionTwoAnswers:            
            print (i + ": " + questionTwoAnswers[i])
            time.sleep(1)
        answerOne = input("Please enter your choice.").upper()
        if answerOne not in Options:
            answerOne = input("Invalid choice, please try again.").upper()
        else:
            if answerOne == "C":
                score += 1
                print ("Correct! Current score: " + str(score) + "/5")
            else:
                print("Incorrect! Current score: " + str(score) + "/5")
                
    elif questionNum == 2:
        print ("Question 2!")
        time.sleep(1)
        print (questionTwo)
        for i in questionTwoAnswers:            
            print (i + ": " + questionTwoAnswers[i])
            time.sleep(1)
        answerOne = input("Please enter your choice.").upper()
        if answerOne not in Options:
            answerOne = input("Invalid choice, please try again.").upper()
        else:
            if answerOne == "C":
                score += 1
                print ("Correct! Current score: " + str(score) + "/5")
            else:
                print("Incorrect! Current score: " + str(score) + "/5")
                
    elif questionNum == 3:
        print ("Question 2!")
        time.sleep(1)
        print (questionTwo)
        for i in questionTwoAnswers:            
            print (i + ": " + questionTwoAnswers[i])
            time.sleep(1)
        answerOne = input("Please enter your choice.").upper()
        if answerOne not in Options:
            answerOne = input("Invalid choice, please try again.").upper()
        else:
            if answerOne == "C":
                score += 1
                print ("Correct! Current score: " + str(score) + "/5")
            else:
                print("Incorrect! Current score: " + str(score) + "/5")
                
    elif questionNum == 4:
        print ("Question 2!")
        time.sleep(1)
        print (questionTwo)
        for i in questionTwoAnswers:            
            print (i + ": " + questionTwoAnswers[i])
            time.sleep(1)
        answerOne = input("Please enter your choice.").upper()
        if answerOne not in Options:
            print("Invalid choice, please try again.")
            
        else:
            if answerOne == "C":
                score += 1
                print ("Correct! Current score: " + str(score) + "/5")
            else:
                print("Incorrect! Current score: " + str(score) + "/5")
                
runQuiz()

    
    
    