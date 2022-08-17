# pypy3 

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution():
    w = int(input())
    res = [0] * (n + 1)
    
    Q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            Q.append(i)
            res[i] += times[i]
            
    while Q:
        v = Q.popleft()
        if v == w:
            return res[v]
        for w in graph[v]:
            res[w] = max(res[w], res[v] + times[w])
            indegree[w] -= 1
            if indegree[w] == 0:
                Q.append(w)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    indegree = [0] * (n + 1)
    times = [0]
    times.extend(list(map(int, input().split())))
    graph = defaultdict(list)
    
    for _ in range(k):
        x, y = map(int, input().split())
        indegree[y] += 1
        graph[x].append(y)
    
    print(solution())