for test_case in range(1, 11):
    n = int(input())
    matrix = [list(input()) for _ in range(8)]
    res = 0

    def solution():
        global res
        for i in range(8):
            for j in range(8):
                if j + n < 9:
                    if matrix[i][j: j + n] == matrix[i][j: j + n][::-1]:
                        res += 1

    solution()
    matrix = list(zip(*matrix))
    solution()

    print(f'#{test_case} {res}')