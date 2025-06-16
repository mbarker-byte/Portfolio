# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 20:32:40 2023

@author: Michael
"""

import threading
import os

def print_cube(num):
    print("print_cube is assignedto thread: {}".format(threading.current_thread().name))
    print("ID of process running print_cube: {}".format(os.getpid()))
    print("Cube: {}".format(num * num * num))
    
def print_square(num):
    print ("print_square is assigned to thread: {}".format(threading.current_thread().name))
    print ("ID of process running print_square: {}".format(os.getpid()))
    print ("Square: {}".format(num * num))
    
if __name__ == "__main__":
    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))
    
    t1 = threading.Thread(target=print_square, args=(10,), name="thread_1")
    t2 = threading.Thread(target=print_cube, args=(10,),name="thread_2")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
    print("Done!")
    
