# pypy3 144808 kb / 380 ms

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
res = [0] * (n + 1)
indegree = [0] * (n + 1)
Q = deque()
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0: # 진입차수가 0이면
        Q.append((i, 1))
        res[i] = 1 # 1학기 이수
        
while Q:
    v, cnt = Q.popleft()
    for w in graph[v]:
        indegree[w] -= 1 # 방문했으니 진입차수 감소
        if indegree[w] == 0:
            Q.append((w, cnt + 1))
            res[w] = cnt + 1
            
print(*res[1:])