# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:26:18 2023

@author: Michael
"""

import collections
graph = {'A': ["B", "C", "G"],
         'B': ["A", "D", "F"],
         'C': ["A", "D"],
         'D': ["B", "C", "E", "K"],
         'E': ["D", "G", "K"],
         'F': ["B", "E", "H"],
         'G': ["A", "H"],
         'H': ["F", "G"],
         'I': ["E", "J"],
         'J': ["I", "J"],
         'K': ["D", "E", "J"]}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        vertex = queue.pop(0)
        print (vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
print("BFS: ")
bfs(visited, graph, 'A')