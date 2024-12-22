# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:24:53 2024

@author: Michael
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def __str__(self):
        return self.data
 
    """allows the linked list to be iterated through, to validate usernames/passwords"""
class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)
    def add(self, item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    

class Credential(LinkedList):
    def __init__(self):
        return self
    def add(self, item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    usernames = LinkedList()       
    passwords = LinkedList()
    """assigning usernames to a linked list"""        
    usernames.add("user1")
    usernames.add("user2")
    usernames.add("user3")
    usernames.add("user4")
    usernames.add("user5")
    usernames.add("user6")
    usernames.add("user7")
    usernames.add("user8")
    usernames.add("user9")
    usernames.add("user10")
    """assigning passwords to a seperate linked list"""
    passwords.add("pass1")
    passwords.add("pass2")
    passwords.add("pass3")
    passwords.add("pass4")
    passwords.add("pass5")
    passwords.add("pass6")
    passwords.add("pass7")
    passwords.add("pass8")
    passwords.add("pass9")
    passwords.add("pass10")

    """searches a linked list for a key word using linear search, then returns it's position in the list, 
    this ensures that usernames and passwords are in the same position in their corresponding linked lists"""
    def indexSearch(self, key):
        count = 0
        for i in self:
            if key != i:
                count +=1
            if key == i:
                return count