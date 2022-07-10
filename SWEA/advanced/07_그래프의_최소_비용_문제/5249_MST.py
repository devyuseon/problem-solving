# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

import sys
sys.stdin = open("SWEA\input.txt", "r")

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    a = find(x)
    b = find(y)
    
    if a == b: return
    else: parents[b] = a
    
def is_union(x, y):
    return find(x) == find(y)
    
T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    edges = []
    parents = [i for i in range(0, v + 1)]
    result = 0
    
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((w, u, v)) # 정렬 편하게 하기 위해 가중치 앞에
    
    edges.sort()
    
    for edge in edges:
        w, u, v = edge
        if not is_union(u, v):
            union(u, v)
            result += w
            
    print(f'#{test_case} {result}')
    