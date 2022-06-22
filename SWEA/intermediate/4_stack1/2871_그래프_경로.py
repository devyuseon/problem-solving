import sys
from collections import defaultdict
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    ans = 0
    
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end) # 단방향
    S, G = map(int, input().split())
    
    stack = [S]
    visited = []
    
    # DFS
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            # 도착 지점이 있는지 검사
            # 이 부분이 일반 DFS랑 다름
            # 그냥 해도 되겠지만 시간 단축
            if G in graph[v]:
                ans = 1
                break
            else:
                for w in graph[v]: 
                    stack.append(w)
            
    print(f'#{test_case} {ans}')
    
    
li = [1, 2, 3, 4, 5]
li = li[0:1] + li[2:]
print(li)