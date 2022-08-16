# pypy3 231348kb / 3160ms

from collections import defaultdict
import heapq

n, m, k, x = map(int, input().split())

def dijkstra():
    Q = [(0, x)] # 가중치, 정점
    
    while Q:
        cost, v = heapq.heappop(Q)
        if v not in dist:
            dist[v] = cost
            for w in graph[v]:
                heapq.heappush(Q, (cost + 1, w))

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
dist = defaultdict(int)
res = [] # 결과

dijkstra() # 다익스트라 수행

for key, val in dist.items():
    if val == k:
        res.append(key)
        
if not res:
    print(-1)
else:
    for i in res: print(i)