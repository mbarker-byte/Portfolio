# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 13:32:45 2025

@author: Michael
"""
import time
import os
clear = lambda: os.system('cls')
taskList = []

"add new tasks to the list"
def addTasks():
        task = input("Enter your task: ")
        taskList.append({"Task": task, "Complete": False})
        print(task + " added!")
        time.sleep(2)
        choice = input("Press 1 to enter a new task, or 2 to return to the menu")
        if choice == "1":
            addTasks()
        elif choice == "2":
            clear()
            main()
        else:
            print("Choice not recognised, returning to menu")
            time.sleep(2)
            main()
        
        
"show tasks existing in the list"
def showTasks():
    print("\nTasks:")
    for task in taskList:
        print (task)
    choice = input("press 1 to return to the menu")
    if choice == "1":
        clear()
        main()
    else:
        print("Choice not recognised, returning to menu")
        time.sleep(2)
        main()
        

"mark tasks as complete"      
def completeTasks():
    Tindex = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= Tindex < len(taskList):
        taskList[Tindex]["Complete"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")
    choice = input("Press 1 to complete a new task, or 2 to return to the menu")
    if choice == "1":
        completeTasks()
    elif choice == "2":
        clear()
        main()
    else:
        print("Choice not recognised, returning to menu")
        time.sleep(2)
        clear()
        main()

"remove tasks from the list"
def removeTasks():
    Tindex = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= Tindex < len(taskList):    
        del taskList[Tindex]
        print("Task removed!")
    else:
        print("Invalid task number.")
        
    time.sleep(2)
    choice = input("Press 1 to remove a new task, or 2 to return to the menu")
    if choice == "1":
        removeTasks()
    elif choice == "2":
        clear()
        main()
    else:
        print("Choice not recognised, returning to menu")
        time.sleep(2)
        main()    
def exit():
    print("Exiting")
    time.sleep(2)
    clear()
    
def main():
    print("Welcome to the to-do List") 
    time.sleep(1)
    print("1. Add new task")
    time.sleep(1)
    print("2. View tasks")
    time.sleep(1)
    print("3. Mark task as complete")
    time.sleep(1)
    print("4. Remove a task")
    time.sleep(1)
       
    choice = input("Enter a choice")
    if choice == "1":
        addTasks()
    elif choice == "2":
        showTasks()
    elif choice == "3":
        completeTasks()
    elif choice == "4":
        removeTasks()
    elif choice == "5":
        exit()
    else:
        print (choice)
        print("Choice not recognised")
        time.sleep(2)
        clear()
        main()
        
main()
    