# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:43:24 2025

@author: Michael
"""

def solution(A):
    # Implement your solution here
    A.sort()
    
    
    number = 1
    tried = []

    for i in A:
        if max(A) <= 0:
            print(1)  
            return
        elif i <= 0:
            print ("neg/0")
            continue
        elif i in tried:
            print ("repeat number")
            continue
        elif i == number:
            tried.append(i)
            number = number + 1
            print ("match")
  
    print(number)
        
    pass
A = [-1, -3, -3]
solution(A)