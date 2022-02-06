import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

# def dfs(node, graph, visited = []):
#     visited.append(node) 

#     for v in graph[node]:
#         if v not in visited:
#             visited = dfs(v, graph, visited)        
    
#     return visited
        

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
Q = deque()
Q.append(1)
visited = [1]

while Q:
    node = Q.popleft()
    for v in graph[node]:
        if v not in visited:
            visited.append(v)
            Q.append(v)

print(len(visited) - 1)

# print(len(dfs(1, graph)) - 1)