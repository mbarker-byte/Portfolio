# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:21:15 2023

@author: Michael
"""

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
            arr[j+1] = key
            
array = [1, 12, 6, 7, 19, 5, 3, 7, 20]

insertionSort(array)


print (array)
