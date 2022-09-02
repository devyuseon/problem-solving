# pypy3 136976kb / 360ms

import sys
from collections import defaultdict
input = sys.stdin.readline

graph = defaultdict(list)
edges = []

n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    edges.append((a, b))

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(graph[k]) < 2: # 자식이 하나밖에 없거나 리프노드 
            print("no")
        else: 
            print("yes")
    if t == 2: # 모든 간선은 단절선
        print("yes")