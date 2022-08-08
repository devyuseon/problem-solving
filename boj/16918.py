# pypy3 207384kb / 588ms

import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def install(sec):
    for i in range(r):
            for j in range(c):
                if matrix[i][j] == '.':
                    matrix[i][j] = sec # sec초에 설치된 폭탄

def explode(sec):
    global r, c
    candidate = []
    for i in range(r):
            for j in range(c):
                if matrix[i][j] != '.':
                    if sec - matrix[i][j] >= 3: # 3초 이상 경과
                        candidate.append((i, j))
    for i, j in candidate:
        matrix[i][j] = '.' # 폭발
        for k in range(4): # 인접한 네칸 폭발
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                matrix[nx][ny] = '.' # 폭발
    
r, c, n = map(int, input().split())
matrix = [['.'] * c for _ in range(r)]
for i in range(r):
    line = list(input())
    for j in range(c):
        if line[j] == 'O':
            matrix[i][j] = 0 # 0초에 설치된 폭탄을 의미

sec = 1 # 처음엔 아무것도 하지 않음

while sec <= n:
    if sec % 2 == 0:
        install(sec)
    if sec % 2 != 0:
        explode(sec)
    sec += 1

for i in range(r):
    for j in range(c):
        if matrix[i][j] != '.':
            print('O', end='')
        else:
            print('.', end='')
    print()