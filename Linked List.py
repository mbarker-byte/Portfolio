# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:10:08 2023

@author: Michael
"""
"""functions as a constructor, will be called when an obkect s created"""
"""Item variable references the data of the node"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        
"""Head variable points to the first element of the list"""
class LinkedList:
    def __init__(self):
        self.head = None
        
"""Creates an instance of the class linked_list, the variable head will be an
object of the node class. The data that needs to be stored needs to be passed as an
argument to the node class. Each node points to the next one"""
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    linked_list.head.next = second
    second.next = third
    
    while linked_list.head != None:
        print (linked_list.head.item, end = " ")
        linked_list.head = linked_list.head.next
        
"""Traverses and prints a linked list"""
def printList(self):
    temp = self.head
    while (temp):
        print (str(temp.data) + " ", end="")
        temp = temp.next
        
"""Inserts a node at the start of a linked list"""
def insertAtBeginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    
"""Inserts  a new node after a specified node"""
def insertAfter(self, prev_node, new_data):
    if prev_node is None:
        print("The given previous node must be inLinkedList")
        return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
"""Inserts a new node at the end of a list"""
def insertAtEnd(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
        last = last.next
    last.next = new_node

"""Deletes a node"""
def deleteNode(self, position):
    if self.head is None:
        return
    temp = self.head
    if position == 0:
        self.head = temp.next
        temp = None
        return
    for i in range(position -1):
        temp = temp.next
        if temp is None:
            break
    if temp is None:
        return
    if temp.next is None:
        return
    next = temp.next.next
    temp.next = None
    temp.next = next
    
"""Searches for an element within the linked list"""
def search(self, key):
    current = self.head
    while current is not None:
        if current.data == key:
            return True
        print(key)
        current = current.next
    return False
    print(key)

"""Revereses a list"""
def reverse(self):
    prev = None
    current = self.head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev
    
search(linked_list, 1)