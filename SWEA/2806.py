T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    res = 0
    col = [0] * n  # col[i] // i: row, col[i]: col

    def is_promising(x):
        for i in range(x):
            # 같은 라인 or 대각선
            if col[i] == col[x] or abs(col[x] - col[i]) == abs(x - i):
                return False
        return True

    def n_queen(x):
        global res

        if x == n:
            res += 1
        else:
            for i in range(n):
                col[x] = i  # 해당 위치에 퀸 배치
                if is_promising(x):  # 유효하다면 다음 행의 퀸 배치, 유효하지 않다면 다른 위치로 퀸 배치 변경
                    n_queen(x + 1)


    n_queen(0)
    print(f'#{test_case} {res}')