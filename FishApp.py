# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:27:00 2026

@author: MBark
"""

import os
import time

clear = lambda: os.system('cls')

testFish = {"season" : "Winter", "weather" : "Rain", "time" : "Morning", "area" : "Beach", "name" : "Test Fish 1" } 

def findFish():
    print ("Welcome to the fish finder!")
    time.sleep(2)
    print("Please enter information when prompted.")
    time.sleep(2)
    print("What season is it?")
    time.sleep(1)
    print("Spring: A")
    time.sleep(1)
    print("Summer: B")
    time.sleep(1)
    print("Autumn: C")
    time.sleep(1)
    print("Winter: D")
    fishSeason = input("Please choose a season:")
    clear()
    time.sleep(2)
    print("What time is it?")
    time.sleep(1)
    print("Morning: A")
    time.sleep(1)
    print("Afternoon: B")
    time.sleep(1)
    print("Night: C")
    time.sleep(1)
    fishTime = input("Please choose a time:")
    clear()
    time.sleep(2)
    
