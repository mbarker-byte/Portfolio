# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 19:07:08 2025

@author: Michael
"""




   

def fizzBuzz(j):
    number = ""
    if str(3) in str(j) or j % 3 == 0:
        number = "Fizz"
    if str(5) in str(j) or j % 5 == 0:
        number += "Buzz"
    if number == "":
        number = str(j)
    return (number)
        
    

def test_num():
    assert fizzBuzz(7) == str(7)   
    assert fizzBuzz(92) == str(92)
    
def test_fizz():
    assert fizzBuzz(8) == "Fizz"
    assert fizzBuzz(13) == "Fizz"
    
def test_buzz():
    assert fizzBuzz(20) == "Buzz"
    assert fizzBuzz(56) == "Buzz"
    
def test_fizzBuzz():
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(53) == "FizzBuzz"

test_num()   
test_fizz()
test_buzz()
test_fizzBuzz()


numList = list(range(1,101))

for i in numList:
    print (fizzBuzz(i))
