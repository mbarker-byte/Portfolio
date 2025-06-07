# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:28:17 2023

@author: Michael
"""

import sys
try:
    f = open("uk.txt")
    if f ==1:
        raise ValueError
    else:
        print("Success")
except (FileNotFoundError):
    print("File not found", sys.ec_info([0]))
