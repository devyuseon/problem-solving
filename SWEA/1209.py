for _ in range(1, 11):
    t = int(input())
    res = 0
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 가로
    for i in range(100):
        res = max(sum(matrix[i]), res)

    # 대각선
    j, _sum = 0, 0
    for i in range(100):
        _sum += matrix[i][j]
        j += 1
    res = max(_sum, res)
    j, _sum = 99, 0
    for i in range(100):
        _sum += matrix[i][j]
        j -= 1
    res = max(_sum, res)

    # 전치행렬
    matrix = list(zip(*matrix))

    # 세로
    for i in range(100):
        res = max(sum(matrix[i]), res)

    print(f'#{t} {res}')