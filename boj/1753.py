# pypy3 168444kb / 976 ms

import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = defaultdict(list)
dist = ["INF"] * (v + 1)    

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 가중치, 도착점
    
def dijkstra():
    heap = ([(0, k)]) # 가중치, 정점
    
    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] == "INF":
            dist[node] = cost
            for c, w in graph[node]:
                alt = cost + c
                heapq.heappush(heap, (alt, w))

dijkstra()
for x in dist[1:]: print(x)