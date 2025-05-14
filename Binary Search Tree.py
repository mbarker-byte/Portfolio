# -*- coding: utf-8 -*-
"""
Created on Wed May 24 22:02:01 2023

@author: Michael
"""
#search function
def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right,key)
    return search(root.left,key)

#node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
#insertion function
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node