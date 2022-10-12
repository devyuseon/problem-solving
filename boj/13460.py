import sys
from collections import deque

input = sys.stdin.readline

board = []
n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def move(i, j, dx, dy):
    c = 0
    while board[i + dx][j + dy] != '#' and board[i][j] != "O":
        # 벽이나 구멍을 만날때까지 이동
        i += dx
        j += dy
        c += 1
    return i, j, c


def bfs():
    while Q:
        rx, ry, bx, by, d = Q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != 'O':  # B가 구멍에 빠지지 않음
                if board[nrx][nry] == "O":  # R만 빠졌으면 탈출 성공
                    print(d)
                    return
                if nrx == nbx and nry == nby: # 만남
                    if rc > bc: # R이 더 많이 이동했을 때. 이동방향이 B와 가까움
                                # 그럼 R이 B보단 덜 이동해야 함
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    Q.append([nrx, nry, nbx, nby, d + 1])
    print(-1)


for i in range(n):
    tmp = list(input())
    board.append(tmp)
    if 'R' in tmp:
        rx, ry = i, tmp.index('R')
    if 'B' in tmp:
        bx, by = i, tmp.index('B')

Q = deque()
Q.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by] = True
bfs()
