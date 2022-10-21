T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, dir, now = 0, 0, 0, 1
    snail = [[0] * n for _ in range(n)]

    while now < n ** 2 + 1:
        snail[x][y] = now
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or \
                snail[nx][ny] != 0:
            dir += 1
            if dir == 4:
                dir %= 4
            nx, ny = x + dx[dir], y + dy[dir]
        x, y = nx, ny
        now += 1

    print(f"#{test_case}")
    for s in snail: print(*s)
