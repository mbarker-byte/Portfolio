# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:00:52 2023

@author: Michael
"""
n = 11
inf = 1 << 60 
dis = [inf] * n
vis = [False] * n
graph = [[0,2,15,0,0,0,11,0,0,0,0],
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

def minDistance(dis, vis):
    min = inf
    for v in range(n):
        if dis[v] < min and vis[v] == False:
            min = dis[v]
            min_index = v
    return min_index

def dijkstra(src):
    dis[src] = 0
    for cout in range(n):
        u = minDistance(dis, vis)
        vis[u] = True
        for v in range(n):
            if (graph[u][v] > 0 and
            vis[v] == False and
            dis[v] > dis[u] + graph[u][v]):
                dis[v] = dis[u] + graph[u][v]
                
src = 0
dijkstra(src)
for _ in range(n):
    print(f"#{_+1} Distance from {src} to {_} is: {dis[_]}")

        