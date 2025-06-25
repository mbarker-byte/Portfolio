# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:05:27 2023

@author: Michael
"""

import multiprocessing
import os
def print_cube(num):
    print ("ID of process running print_cube: {}".format(os.getpid()))
    print("Cube: {}".format(num * num * num))
    
def print_square(num):
    print ("ID of process running print_square: {}".format(os.getpid()))
    print("Square: {}".format(num * num))
    
if __name__ =="__main__":
    print("ID of main process: {}".format(os.getpid()))
    p1 = multiprocessing.Process(target=print_cube, args=(10,))
    p2 = multiprocessing.Process(target=print_square, args=(10,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Both processes finished execution!")
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    print("Done!")