# pypy3 216516kb / 14192ms

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i):
    Q = deque([i])
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    cnt = 1
    while Q:
        v = Q.popleft()
        for w in graph[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True
                cnt += 1
    return cnt
    
        
n, m  = map(int, input().split())
graph = [set() for i in range(n + 1)]
res = [0 for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].add(a)

for i in range(1, n + 1):
    res[i] = bfs(i)
    
_max = max(res)
for i in range(n + 1):
    if res[i] == _max: print(i, end = ' ')