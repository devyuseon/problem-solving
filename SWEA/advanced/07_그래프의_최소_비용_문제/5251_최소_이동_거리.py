# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

import sys
from collections import defaultdict
import heapq
sys.stdin = open("SWEA\input.txt", "r")

def dijkstra(start):
    Q = [(0, start)] # 가중치, 시작점
    
    while Q:
        cost, node = heapq.heappop(Q)
        if dist[node] is None: # 방문하지 않음
            dist[node] = cost
            for w, v in graph[node]:
                alt = cost + w
                heapq.heappush(Q, (alt, v))

T = int(input())
for test_case in range(1, T + 1):
    n, e = map(int, input().split()) # 도착점, 간선 수
    dist = [None] * (n + 1)
    graph = defaultdict(list)
    for _ in range(e):
        u, v, w = map(int, input().split()) # 시작, 끝, 가중치 '일방통행'
        graph[u].append((w, v)) # 가중치, 도착점
    
    dijkstra(0)
            
    print(f'#{test_case} {dist[n]}')
    