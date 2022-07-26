# pypy3 136144kb / 316ms

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
parent = [0 for _ in range(n + 1)] # 부모 노드 표시
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS    
Q = deque([1])

while Q:
    node = Q.popleft()
    for i in graph[node]:
        if parent[i] == 0:
            parent[i] = node
            Q.append(i)

for i in parent[2:]:
    print(i)