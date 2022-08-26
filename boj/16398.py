# pypy3 295476kb / 4548ms

import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
        
def is_union(x, y):
    return find(x) == find(y)

n = int(input())
edges = []
parents = [i for i in range(n + 1)]

for i in range(n):
    for j, v in enumerate(list(map(int, input().split()))):
        if i != j:
            edges.append((v, i, j))
    
edges.sort() # 비용순 오름차순 정렬

result = 0
for edge in edges:
    c, i, j = edge
    
    if not is_union(i, j):
        union(i, j)
        result += c

print(result)