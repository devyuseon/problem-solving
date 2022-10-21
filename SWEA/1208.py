for test_case in range(1, 11):
    n = int(input())
    matrix = list(map(int, input().split()))
    matrix.sort()

    for _ in range(n):
        matrix[0] += 1
        matrix[99] -= 1
        matrix.sort()

    print(f"#{test_case} {matrix[99] - matrix[0]}")
