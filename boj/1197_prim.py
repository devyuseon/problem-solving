from collections import defaultdict
from sys import stdin
import heapq

graph = defaultdict(list)
connected = []

V, E = map(int, input().split())
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((w, u, v)) # 가중치, 시작, 도착
    graph[v].append((w, v, u)) # 무방향 그래프

def prim(start):
    connected.append(start)
    neighbors = graph[start]
    heapq.heapify(neighbors)
    mst = []
    result = 0
    
    while neighbors:
        w, u, v = heapq.heappop(neighbors)
        if v not in connected:
            connected.append(v)
            mst.append((u, v))
            result += w
            
            for edge in graph[v]:
                if edge[2] not in connected:
                    heapq.heappush(neighbors, edge)
                    
    return result

print(prim(1))