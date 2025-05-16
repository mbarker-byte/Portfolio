# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:05:47 2023

@author: Michael
"""

class Super:
    var1 = None
    _var2 = None
    __var3 = None
    
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def displayPublicMembers(self):
        print ("public Data Member: ", self.var1)    
    
    def _displayProtectedMembers(self):
        print ("Protected Data Member: ", self._var2)
 
    def __displayPrivateMembers(self):
        print ("Private Member Data: ", self.__var3)
        
    def accessPrivateMembers(self):
        self.__displayPrivateMembers()
    

class Sub(Super):
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)
    def accessProtectedMembers(self):
        self._displayProtectedMembers()
        
obj = Sub("ABC", 4, "EFG!")

obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

print("Object is accessing protected member:", obj._var2)

print(obj.__var3)