import sys
from collections import deque
input = sys.stdin.readline

# n: 세로, m: 가로
n, m, k = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = -sys.maxsize

def bfs(x, y):
    count = 1
    Q = deque([(x, y)])
    visited[x][y] = True
    
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    Q.append((nx, ny))
                    count += 1
    return count
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not visited[i][j]:
            result = max(result, bfs(i, j))
            
print(result)