# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:37:26 2023

@author: Michael
"""

def binarySearch(arr, l, r, x):
    if r >=1:
        mid = l + (r -l) // 2
        
        if arr[mid] == x: 
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, 1, mid-1, r, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return-1
        
arr=[1, 3, 5, 6, 7, 10, 11, 14, 16, 20]
x = 14

result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index % d" % result)
    