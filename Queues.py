# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:37:58 2023

@author: MBark
"""

def __init__(self):
    self.queue=[]
    
def enqueue(self, item):
    self.queue.append(item)
    
def dequeue(self):
    if len(self.queue) < 1:
        return None
    return self.queue.pop(0)

def display(self):
    print(self.queue)
    
