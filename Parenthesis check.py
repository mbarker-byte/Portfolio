# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:39:42 2023

@author: Michael
"""

def check(myStr):
    stack = []
    for i in myStr:
        if i == "(":
            stack.append(i)
        elif i ==")":
            if (len(stack) <= 0):
                return "Unbalanced"
            else:
                stack.pop()
    if len(stack) == 0:
        return "balanced"
    else:
        return "Unbalanced"
            