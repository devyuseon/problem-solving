for test_case in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for j in range(n):
        stack = []
        for i in range(n):
            if not stack and matrix[i][j] == 1:
                stack.append(1)
            elif stack and matrix[i][j] == 2:
                res += stack.pop()

    print(f'#{test_case} {res}')