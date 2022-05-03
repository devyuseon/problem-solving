from sys import stdin

V, E = map(int, input().split())

edges = []
parent = [i for i in range(V + 1)]
result = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b: return
    else: parent[b] = a
    
def is_union(a, b):
    if find(a) == find(b): return True
    else: return False

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    edges.append((w, v, u)) # 가중치, 시작, 도착

edges.sort() # 오름차순 정렬

for edge in edges:
    w, u, v = edge
    if not is_union(u, v):
        union(u, v)
        result += w

print(result)