# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:31:39 2023

@author: Michael
"""
from threading import Thread
import numpy as np

def increaseByOne(array):
    array += 1
    
data = np.ones((100,1))
increaseByOne(data)

print(data[0])

t = Thread(target=increaseByOne, args=(data,))
t.start()
t.join()

print(data[0])