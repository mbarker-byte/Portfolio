import os
import time
import csv

clear = lambda: os.system('cls')

#TODO add logic for multiple values per key and any values: change identifying if statements to contains rather than ==
#TODO use lists instead of strings for values, use 

testFish = [{"season" : "Summer", "time" : "Afternoon", "weather" : "Sun", "name" : "Pufferfish", "area" : "Ocean/Island" },
            {"season" : "Spring/Fall", "time" : "Anytime", "weather" : "Any", "name" : "Anchovy", "area" : "Ocean" },
            {"season" : "Summer/Winter", "time" : "Morning/Afternoon", "weather" : "Any", "name" : "Tuna", "area" : "Ocean/Island" },
            {"season" : "Spring/Fall/Winter", "time" : "Morning/Afternoon", "weather": "Any", "name" : "Sardine", "area" : "Ocean/sland"},
            {"season" : "All", "time" : "Night", "weather": "Any", "name" : "Bream", "area" : "Ocean"},
            {"season" : "All", "time" : "Morning/Afternoon", "weather": "Any", "name" : "Largemouth Bass", "area" : "Mountain Lake"},
            {"season" : "Spring/Fall", "time" : "Any", "weather": "Any", "name" : "Smallmouth Bass", "area" : "Town River/Forest Pond"},
            {"season" : "Summer", "time" : "Anyt", "weather": "Sun", "name" : "Rainbow Trout", "area" : "Town River/ Forest River/ Mountain Lake"},
            {"season" : "Fall", "time" : "Any", "weather": "Any", "name" : "Salmon", "area" : "Town River/Forest River/Forest Waterfalls"},
            {"season" : "", "time" : "", "weather": "", "name" : "", "area" : ""},
            ]


legendaryFish=[]

def getFish():
    fishList = []
    with open('fish.csv') as csvfile:
        fishReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for fish in fishReader:
            fishList.append(fish)
    return fishList

class Fish:
    def __init__(self, fishSeason, fishTime, fishWeather, fishName, fishArea):
        self.fishSeason = fishSeason
        self.fishTime = fishTime
        self.fishWeather = fishWeather
        self.fishName = fishName
        self.fishArea = fishArea
        

        

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
    else:
        print("Thanks for choosing a season!")
        time.sleep(2)
        clear()
        time.sleep(2)
        if fishSeason == "a":
            return "Spring"
        elif fishSeason ==  "b":
            return "Summer"
        elif fishSeason == "c":
            return "Autumn"
        elif fishSeason == "d":
            return "Winter"
         
    
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
    if fishTime not in ('a', 'b', 'c'):
        print("Invalid option, please try again.")
        time.sleep(2)
        clear()
        fishTime()
    else:
        print("Thanks for choosing a time!")
        time.sleep(2)
        clear()
        time.sleep(2)
        if fishSeason == "a":
            return "Morning"
        elif fishSeason ==  "b":
            return "Afternoon"
        elif fishSeason == "c":
            return "Night"
    
def fishWeather():
    print("What is the weather like?")
    time.sleep(1)
    print("Rain/Snow: A")
    time.sleep(1)
    print("Clear: B")
    time.sleep(1)
    print("Stormy: C")
    time.sleep(1)
    fishWeather = input("Please choose the weather.").lower()
    if fishWeather not in ('a', 'b'):
        print("Invalid option, please try again.")
        time.sleep(2)
        clear()
        fishWeather()
    else:
        print("Thanks for choosing the weather!")
        time.sleep(2)
        clear()
        time.sleep(2)
        if fishSeason == "a":
            return "Rain"
        elif fishSeason ==  "b":
            return "Clear"
        elif fishSeason == "c":
            return "Stormy"

            

def fishMenu():
    print ("Welcome to the fish finder!")
    time.sleep(2)
    print ("Do you want to find legendary or regular fish?")
    time.sleep(1)
    print("Legendary: A")
    time.sleep(1)
    print("Regular: B")
    time.sleep(1)
    choice = input("Please Choose your fish type.").lower()
    if choice not in ('a', 'b'):
        print ("invalid option, please try again.")
        time.sleep(2)
        clear()
        fishMenu()
    else:
        if choice == 'a':
            print ("Loading legendary fish...")
            time.sleep(2)
            clear()
            legendaryFish()
        if choice =='b':
            print ("Loading regular fish...")
            time.sleep(2)
            clear()
            regularFish()
        
#Add logic to convert letter choices to a string value
def regularFish():
    print("Please enter information when prompted.")
    time.sleep(2)
    s = fishSeason()    
    t = fishTime()
    w = fishWeather()
    catchableFish = []
    
    for fish in testFish:
        if fish["season"] == s:
            if fish["time"] == t:
                if fish["weather"] == w:
                    catchableFish.append(fish)
                    
    time.sleep(1)
    if len(catchableFish) == 0:
        print("There are no fish for you to catch today")
    else:
        print("You can catch the following fish")
        for fish in catchableFish:
            print(catchableFish["name"] + " in the " + catchableFish["area"])
            time.sleep(1)
            
    time.sleep(2)
    print ("would you like to go again?")
    answer = input("Y/N?").lower()
    if answer == "y":
        fishMenu()
    else:
        return
    
def legendaryFish():
    print("Please enter information when prompted")
        
    
fishMenu()
