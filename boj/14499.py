import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

ver = deque([0, 0, 0, 0])
hos = deque([0, 0, 0, 0])

n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for d in list(map(int, input().split())):
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    else:
        x, y = nx, ny

    dice = 0

    if d in [1, 2]:
        dice = hos[1 + dy[d]]
        hos.rotate(dy[d] * (-1))
        ver[1] = hos[1] # 아랫면 숫자
        ver[3] = hos[3]
    else:
        dice = ver[1 + dx[d]]
        ver.rotate(dx[d] * (-1))
        hos[1] = ver[1]
        hos[3] = ver[3]

    if matrix[x][y] == 0:
        matrix[x][y] = dice
    else:
        ver[1], hos[1] = matrix[x][y], matrix[x][y]
        matrix[x][y] = 0

    print(ver[3])