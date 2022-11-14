import copy

matrix = [list(map(int, input().split())) for _ in range(5)]
garo, sero = [0] * 5, [0] * 5
degak = [0, 0]  # \, /
memo = [[0] * 5 for _ in range(5)]
cnt = 0

dx = [1, 1]
dy = [1, -1]


def check(m):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == m:
                memo[i][j] = 1
                return


def bingo():
    global cnt

    # 가로
    for i, v in enumerate(memo):
        if not garo[i]:
            if sum(v) == 5:
                garo[i] = 1
                cnt += 1
                if cnt == 3: return True

    # 세로
    tmp = copy.deepcopy(memo)
    tmp = zip(*tmp)
    for i, v in enumerate(tmp):
        if not sero[i]:
            if sum(v) == 5:
                sero[i] = 1
                cnt += 1
                if cnt == 3: return True

    # 대각선 \
    x, y = 0, 0
    if memo[x][y] and not degak[0]:
        _sum = 0
        for _ in range(4):
            nx, ny = x + dx[0], y + dy[0]
            if memo[nx][ny] == 1:
                _sum += 1
            else:
                break
        if _sum == 4:
            degak[0] = 1
            cnt += 1
            if cnt == 3: return True

    # 대각선 /
    x, y = 0, 4
    if memo[x][y] and not degak[1]:
        _sum = 0
        for _ in range(4):
            nx, ny = x + dx[1], y + dy[1]
            if memo[nx][ny] == 1:
                _sum += 1
            else:
                break
        if _sum == 4:
            degak[1] = 1
            cnt += 1
            if cnt == 3: return True

    return False


def solution():
    for i in range(5):
        for j, v in enumerate(list(map(int, input().split()))):
            t = 5 * i + (j + 1)
            check(v)
            if bingo():
                print(t)
                return


solution()
