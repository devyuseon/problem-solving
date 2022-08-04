# pypy3 233952kb / 680ms

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(Q: deque):
    global n, m
    
    result = 0
    visited = [[False] * n for _ in range(m)]
    for x, y, day in Q:
        visited[x][y] = True # 익은 토마토 방문표시
    
    while Q:
        x, y, day = Q.popleft()
        result = max(result, day)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and matrix[nx][ny] != -1:
                    Q.append((nx, ny, day + 1))
                    matrix[nx][ny] += 1
                    visited[nx][ny] = True
                    
    return result
                    
def search():
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0: # 하나라도 안익은 토마토 있으면 False
                return False
    return True
            
n, m = map(int, input().split())
matrix = [] # 토마토 창고
tomato = deque() # 익은토마토들

for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            tomato.append((i, j, 0)) # x, y, day -> bfs 시작큐
    matrix.append(tmp)
    
day = bfs(tomato)

if search():
    print(day)
else:
    print(-1)