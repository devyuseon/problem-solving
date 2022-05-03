# 간선의 갯수 : M
# 노드(마을) 갯수 : N
# X : 이번에 파티하는 마을 (출발점)
# N, M, X / 시작점, 끝점, 가중치

from collections import defaultdict
import heapq
from sys import stdin

graph = defaultdict(list)
dist_to_home = defaultdict(int)
result = defaultdict(int)

N, M, X = map(int, input().strip().split())
for _ in range(M):
    u, v, w = map(int, stdin.readline().strip().split())
    graph[u].append((v, w)) # 끝점, 가중치

def dijkstra(start, end):
    global dist_to_home
    
    Q = [(0, start)] # 가중치, 시작점
    dist = defaultdict(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = w + time
                heapq.heappush(Q, (alt, v))
    
    return dist[end]

max_len = 0
for n in range(1, N + 1):
    max_len = max(max_len, dijkstra(n, X) + dijkstra(X, n))

print(max_len)