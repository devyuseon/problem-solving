# pypy3 217992kb / 1432ms

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
matrix = []
machine = [] # 공기청정기 위치
for i in range(r):
    line = list(map(int, input().split()))
    matrix.append(line)
    if -1 in line: # 공기청정기가 있으면
        j = line.index(-1)
        machine.append(i)        

while t > 0:

    #---------------------------------------------------
    
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    total = dict()
    for i in range(r):
        for j in range(c):
            if matrix[i][j] != -1 and matrix[i][j] > 0:
                tmp = []
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    # 1. 범위 안에 있고
                    # 2. 공기청정기 위치가 아님
                    if 0 <= x < r and 0 <= y < c and \
                        matrix[x][y] != -1: 
                        tmp.append((x, y))
                total[(i, j, matrix[i][j])] = tmp
    # 확산 과정
    for i, j, mise in total.keys():
        new = mise // 5 # 확산되는 양
        spread = total[(i, j, mise)]
        for x, y in spread: 
            matrix[x][y] += new
        matrix[i][j] -= new * len(spread) # (r, c)에 남은 미세먼지의 양
    
    #---------------------------------------------------
    
    n = machine[0]
    for i in range(n - 1, 0, -1):
        matrix[i][0] = matrix[i - 1][0]
    for i in range(n + 2, r - 1):
        matrix[i][0] = matrix[i + 1][0]
    for i in range(c - 1):
        matrix[0][i] = matrix[0][i + 1]
        matrix[r - 1][i] = matrix[r - 1][i + 1]
    for i in range(n):
        matrix[i][c - 1] = matrix[i + 1][c - 1]
    for i in range(r - 1, n + 1, -1):
        matrix[i][c - 1] = matrix[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        matrix[n][i], matrix[n + 1][i] = matrix[n][i - 1], matrix[n + 1][i - 1]
    matrix[n][1] = 0
    matrix[n + 1][1] = 0
    
    #---------------------------------------------------
    
    t -= 1

_sum = 0
for line in matrix:
    _sum += sum(line)
print(_sum + 2)