T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    res = [[0] * n for _ in range(n)]
    res[0][0] = 1

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                res[i][j] = res[i - 1][j]
            elif i == j:
                res[i][j] = res[i - 1][j - 1]
            else:
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

    print(f'#{test_case}')
    for i in range(n):
        print(*res[i][:i + 1])