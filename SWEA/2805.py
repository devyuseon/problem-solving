T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(n)]
    start = n // 2
    size = 1
    idx = 0
    res = 0

    while idx < n:
        res += sum(matrix[idx][start: start + size])
        if idx < n // 2:
            size += 2
            start -= 1
        else:
            size -= 2
            start += 1
        idx += 1

    print(f'#{test_case} {res}')