# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:11:34 2024

@author: Michael
"""

import calendar
import time



def programme():
    userChoice = int(input("Enter 1 for a yearly calander or 2 for a month:"))
    if userChoice == 1:
        userYear = int(input("Please enter the year:"))
        print(calendar.calendar(userYear))
        time.sleep(3)
        restart = int(input("Press 1 to start again"))
        if restart == 1:
            programme()
        else:
             print("Input not recognised")
             return
    elif userChoice == 2:
        userYear = int(input("Please enter the year:"))
        userMonth = int(input("Please enter the month:"))
        print(calendar.month(userYear, userMonth))
        time.sleep(3)
        restart = int(input("Press 1 to start again"))
        if restart == 1:
            programme()
        else:
            print("Input not recognised")
            return
            
    else:
        print("Input not recognised, please try again.")
        programme()

programme()