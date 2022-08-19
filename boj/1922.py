# pypy3 129328kb / 428ms

import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def is_union(x, y):
    return find(x) == find(y)

n = int(input())
m = int(input())
edges = []
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # 가중치, 출발, 도착

edges.sort() # 오름차순 정렬
res = 0

for w, u, v in edges:
    if not is_union(u, v):
        union(u, v)
        res += w

print(res)