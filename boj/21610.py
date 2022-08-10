# pypy3 118876kb / 232ms

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
move = [tuple(map(int, input().split())) for _ in range(m)]
cloud = deque([[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]])

#  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for d, s in move: 
    # 모든 구름이 di 방향으로 si칸 이동한다.
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다
    visited = [[False] * n for _ in range(n)]
    l = len(cloud)
    for _ in range(l):
        x, y = cloud.popleft()
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        matrix[nx][ny] += 1
        visited[nx][ny] = True
        cloud.append([nx, ny])
    
    # 구름이 모두 사라진다.
    
    # 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
    for x, y in cloud:
        for i in [2, 4, 6, 8]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] > 0:
                    matrix[x][y] += 1
                    
    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고
    # 물의 양이 2 줄어든다
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    cloud = deque()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] >= 2 and [i, j] and not visited[i][j]:
                matrix[i][j] -= 2
                cloud.append([i, j])

print(sum(sum(n) for n in matrix))


'''
구름이었는지 조회할때 in cloud 문법써서 조회하면 시간초과 발생
visited 배열로 체크해야함
'''