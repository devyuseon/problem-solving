# pypy3 235972kb / 800ms

import sys
from collections import defaultdict
input = sys.stdin.readline

n, w = map(int, input().split())
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for k, v in graph.items():
    # 간선이 하나고 루트노드가 아님 (리프노드)
    if len(v) == 1 and k != 1:
        cnt += 1

print(w / cnt)