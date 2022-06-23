import sys
from collections import defaultdict
from collections import deque
sys.stdin = open("SWEA\input.txt", "r")

def bfs(start, end):
    Q = deque([(start, 0)])
    
    while Q:
        v, cnt = Q.popleft()
        visited.append(v)
        
        for w in graph[v]:
            if w not in visited and w == end:
                return cnt + 1
            elif w not in visited:
                Q.append((w, cnt + 1))
    
    return 0 # 못감
    
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    visited = [S] # 방문 체크
       
    print(f'#{test_case} {bfs(S, G)}')