# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:27:00 2026

@author: MBark
"""

import os
import time
import csv

clear = lambda: os.system('cls')

testFish = [{"season" : "Winter", "time" : "Morning", "weather" : "Rain", "name" : "Test Fish 1" },
            {"season" : "Summer", "time" : "Afternoon", "weather" : "Rain", "name" : "Test Fish 1" },
            {"season" : "Spring", "time" : "Night", "weather" : "Rain", "name" : "Test Fish 1" }
            ]

def getFish():
    fishList = []
    with open('fish.csv') as csvfile:
        fishReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for fish in fishReader:
            fishList.append(fish)
    return fishList

class Fish:
    def __init__(self, fishSeason, fishTime, fishWeather, fishName):
        self.fishSeason = fishSeason
        self.fishTime = fishTime
        self.fishWeather = fishWeather
        self.fishName = fishName
        
testFishObject = Fish(testFish["season"], testFish["time"], testFish["weather"], testFish["name"])

print (testFishObject)
print (testFishObject.fishSeason)
print (testFishObject.fishTime)
print (testFishObject.fishWeather)
print (testFishObject.fishName)
        

def fishSeason():
    print("What season is it?")
    time.sleep(1)
    print("Spring: A")
    time.sleep(1)
    print("Summer: B")
    time.sleep(1)
    print("Autumn: C")
    time.sleep(1)
    print("Winter: D")
    fishSeason = input("Please choose a season:").lower()
    if fishSeason not in ('a', 'b', 'c', 'd'):
        print("Invalid option, please try again.")
        time.sleep(2)
        clear()
        fishSeason()
    clear()
    time.sleep(2)
    return fishSeason
    
def fishTime():
    print("What time is it?")
    time.sleep(1)
    print("Morning: A")
    time.sleep(1)
    print("Afternoon: B")
    time.sleep(1)
    print("Night: C")
    time.sleep(1)
    fishTime = input("Please choose a time:").lower()
    if fishSeason not in ('a', 'b', 'c'):
        print("Invalid option, please try again.")
        time.sleep(2)
        clear()
        fishSeason()
    clear()
    time.sleep(2)
    return fishTime
    
def fishWeather():
    print("Please choose the current weather:")
    time.sleep(1)
    print("Rain/Snow: A")
    time.sleep(1)
    print("Clear: B")
    time.sleep(1)
    print("Stormy: C")
    time.sleep(1)
    fishWeather = input("Please choose the weather.").lower()
    if fishSeason not in ('a', 'b'):
        print("Invalid option, please try again.")
        time.sleep(2)
        clear()
        fishSeason()
    clear()
    time.sleep(2)
    return fishWeather

            

def findFish():
    print ("Welcome to the fish finder!")
    time.sleep(2)
    print("Please enter information when prompted.")
    time.sleep(2)
    s = fishSeason()    
    t = fishTime()
    w = fishWeather()
    for  in testFish:
        if testFish["season"] == fishSeason():
            if testFish["time"] == fishTime():
                if testFish["weather"] == fishWeather():
                    print ("You can catch " + testFish["name"] + at testFish["area"])
    
