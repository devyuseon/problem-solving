import sys
from typing import List

sys.setrecursionlimit(10 ** 8)

def dfs(x: int, y: int):
    # 배추가 아님
    if x < 0 or x >= N or \
        y < 0 or y >= M :
        return False
    
    # 배추임
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문

        dfs(x, y + 1) # 상
        dfs(x, y - 1) # 하
        dfs(x - 1, y) # 좌
        dfs(x + 1, y) # 우 

        return True
    
    return False



T = int(input())
result = []

for i in range(T) :
    M, N, K =  map(int, sys.stdin.readline().split())
    graph = [[0] * M for i in range(N)] # 0 으로 초기화

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1 # 배추 있는곳 1
    
    count = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if dfs(i, j):
                    count += 1

    result.append(count)

for n in result:
    print(n)