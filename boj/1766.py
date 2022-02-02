import sys
import collections
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = collections.defaultdict(list)
indegree = [0] * (n + 1) # 진입 차수 테이블

result = []
Q = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(Q, i)

while Q:
    node = heapq.heappop(Q)
    result.append(node)
    for _next in graph[node]:
        indegree[_next] -= 1
        if indegree[_next] == 0:
            heapq.heappush(Q, _next)

print(*result)