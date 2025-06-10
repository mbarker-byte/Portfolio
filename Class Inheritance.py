# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:26:10 2023

@author: Michael
"""

class Parent:
    name = ""
    def __init__(self):
        print ("Parent class constructor")
        pass
    def set_country_name(self, name):
        self.name = name
        
class Child(Parent):
    currency = ""
    def __init__(self):
        print("Child class constructor")
        pass
    def set_currency(self, currency):
        self.currency = currency
    def print_data(self):
        print(self.name)
        print(self.currency)
            
obj = Child()
obj.set_country_name("UK")
obj.set_currency("Pound")
obj.print_data