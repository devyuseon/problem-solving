# pypy3 132368kb / 2212ms

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, m):
    global k, l, r, change
    
    Q = deque([(n, m)]) # 행, 열
    visited[n][m] = True
    countries = [(n, m)]
    population = matrix[n][m]

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < k and 0 <= ny < k:
                if not visited[nx][ny] and \
                    l <= abs(matrix[x][y] - matrix[nx][ny]) <= r:
                        Q.append((nx, ny))
                        countries.append((nx, ny))
                        population += matrix[nx][ny]
                        visited[nx][ny] = True
    
    if len(countries) > 1:
        change = True
        move(countries, population)
                    
def move(countries, population):
    new = population // len(countries)
    for x, y in countries:
        matrix[x][y] = new
         

k, l, r = map(int, input().split())
matrix = []
day = 0
change = True

for _ in range(k):
    matrix.append(list(map(int, input().split())))

while change:
    change = False
    visited = [[False] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if not visited[i][j]:
                bfs(i, j)
    if change:
        day += 1
print(day)