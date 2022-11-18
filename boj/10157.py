c, r = map(int, input().split())
k = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

matrix = [[0] * (c + 1) for _ in range(r + 1)]


def solution():
    if k > c * r:
        print(0)
        return

    d = 0
    x, y = 1, 1

    for _ in range(k - 1):
        matrix[x][y] = 1
        nx, ny = x + dx[d], y + dy[d]
        if nx < 1 or nx > r or ny < 1 or ny > c or matrix[nx][ny]:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]
        x, y = nx, ny

    print(y, x)


solution()