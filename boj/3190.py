import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 수
matrix = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
snake = deque([[0, 0]])
d = 1  # 처음 진행 방향

for _ in range(k):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = 2  # 사과


def move():  # 이동 한번
    flag = False  # 사과 먹었는지 여부

    x, y = snake[0]
    nx, ny = x + dx[d], y + dy[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return False
    if matrix[nx][ny] == 1:
        return False

    if matrix[nx][ny] == 2:
        flag = True

    matrix[nx][ny] = 1
    snake.appendleft([nx, ny])

    if not flag:
        px, py = snake.pop()
        matrix[px][py] = 0 # 지움

    return True


def solution():
    global d

    t = 0  # 시간

    l = int(input())

    for _ in range(l):
        x, c = input().split()

        while t < int(x):
            t += 1
            if not move():
                return t

        if c == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

    while True:
        t += 1
        if not move(): break

    return t


print(solution())
