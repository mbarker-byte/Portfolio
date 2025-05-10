# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:44:41 2023

@author: Michael
"""

pgraph= [[0,2,15,0,0,0,11,0,0,0,0],
        [2,0,0,5,0,6,0,0,0,0,0],
        [15,0,18,0,0,0,0,0,0,0,0],
        [0,5,18,0,6,0,0,0,0,0,11],
        [0,0,0,6,0,5,0,0,0,0,12],
        [0,6,0,0,5,0,0,1,0,0,0],
        [11,0,0,0,0,0,0,3,0,0,0],
        [0,0,0,0,0,1,3,0,0,0,0],
        [0,0,0,0,13,0,0,0,0,5,0],
        [0,0,0,0,0,0,0,0,5,0,37],
        [0,0,0,11,12,0,0,0,0,37,0]
        ]


    
inf = 9999
n = 11
key = [inf] * n
parent = [None] * n
vis = [False] * n
key[0] = 0
parent[0] = -1


        
def printMST(parent):
    print ("Edge \tWeight")
    for i in range(1, n):
        print (parent[i], "-", i, "\t", pgraph[i][parent[i]])

def minKey(key, vis):
    min = inf
    for v in range(n):
        if key[v] < min and vis[v]==False:
            min = key[v]
            min_index = v
    return min_index    

def primMST():
    key[0] = 0
    parent[0] = -1
    for cout in range(n):
        u = minKey(key, vis)
        vis[u] = True
        for v in range(n):
            if pgraph[u][v] > 0 and vis[v] == False and key[v] > pgraph[u][v]:
                key[v] = pgraph[u][v]
                parent[v] = u
    printMST(parent)
    
primMST()
            
    