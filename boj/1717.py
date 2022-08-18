import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
parent = {i for i in range(n + 1)}

def union(x, y):
    x = find(a)
    y = find(b)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
def find(x):
    # 루트 노드 찾을때까지
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
        
for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    if cal == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")