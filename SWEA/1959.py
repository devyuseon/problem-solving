T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # len(A) < len(B) 로 만들기
    if len(A) > len(B):
        A, B = B, A

    start, res = 0, 0
    a, b = len(A), len(B)
    for _ in range(b - a + 1):
        _sum = 0
        for i in range(a):
            _sum += A[i] * B[start + i]
        res = max(_sum, res)
        start += 1

    print(f'#{test_case} {res}')