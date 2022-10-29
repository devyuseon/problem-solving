T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        board.append([0] + list(map(int, input().split())))
    res = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            board[i][j] = board[i-1][j] + board[i][j]

    for i in range(1, n - m + 2):
        for j in range(1, n - m + 2):
            res = max(res, sum(board[i + m - 1][j: j + m]) - sum(board[i - 1][j: j + m]))

    print(f'#{test_case} {res}')