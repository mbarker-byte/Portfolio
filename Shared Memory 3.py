# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:48:10 2023

@author: Michael
"""

from threading import Thread
import numpy as np
from threading import Lock

lock = Lock()

def increaseByOne(array):
    lock.acquire()
    for i in range(len(array)):
        array[i] +=1
    lock.release()
    
def divide(array):
    lock.acquire()
    for i in range(len(array)):
        array[i] /= 1.1
    lock.release()
    
data = np.ones((100000,1))

t = Thread(target=increaseByOne, args=(data,))
t2= Thread(target=divide, args=(data,))
t.start()
t2.start()
t.join()
t2.join()
print(np.max(data))
print(np.min(data))