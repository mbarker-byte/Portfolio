# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 21:04:44 2023

@author: Michael
"""

n = 5
g = []
result = []
parent = []
rank = []

def addEdge(u, v, w):
    g.append([u, v, w])
    
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
        
def KruskalMST():
    graph = sorted(g, key=lambda item: item[2])
    for node in range(n):
        parent.append(node)
        rank.append(0)
    minimumCost, e, i = 0, 0, 0
    while e < n - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e +1
            result.append([u, v, w])
            minimumCost += w
            union(parent, rank, x, y)
    return minimumCost

addEdge(4, 1, 10)
addEdge(0, 2, 6)
addEdge(0, 3, 5)
addEdge(1, 3, 15)
addEdge(2, 3, 4)




print("Minimum Spanning Tree", KruskalMST())
print ("Edges in the constructed MST")
for u, v, weight in result:
    print("%d -- %d == %d" % (u, v, weight))
