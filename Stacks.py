# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:25:26 2023

@author: Michael
"""

def create_stack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)
    
def check_empty(stack):
    return len(stack) == 0
    
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    return stack.pop()