import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check = [False for i in range(91)]


def dfs(x, y, cnt):
    global res

    res = max(res, cnt)
    check[ord(matrix[y][x])] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if not check[ord(matrix[ny][nx])]:
                dfs(nx, ny, cnt + 1)

    check[ord(matrix[y][x])] = False


dfs(0, 0, 1)

print(res)


'''
<시간초과>

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check = set()


def dfs(x, y, cnt):
    global res

    res = max(res, cnt)
    check.add(matrix[y][x])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if matrix[ny][nx] not in check:
                dfs(nx, ny, cnt + 1)

    check.remove(matrix[y][x])


dfs(0, 0, 1)

print(res)


'''