# pypy3 271132kb / 5068ms

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

n, m = map(int, input().split())
edges = []
parents = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c, = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort() # 비용순 오름차순 정렬

result = 0
_max = -sys.maxsize
for edge in edges:
    c, a, b = edge
    
    if not is_union(a, b):
        union(a, b)
        result += c
        _max = max(_max ,c)

print(result - _max)