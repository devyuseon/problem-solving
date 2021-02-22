import sys
from collections import defaultdict

N = int(input()) # 노드(컴퓨터) 수
M = int(input()) # 간선(컴퓨터 쌍)의 수

computer = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)

discoverd = []
stack = [1]

# DFS
while stack:
    v = stack.pop()
    if v not in discoverd:
        discoverd.append(v)
        for w in computer[v]:
            stack.append(w) 

print(len(discoverd) - 1)