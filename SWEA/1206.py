for test_case in range(1, 11):

    n = int(input())
    height = list(map(int, input().split()))
    res = 0

    for i in range(2, n - 2):
        left = max(height[i - 2], height[i - 1])
        right = max(height[i + 1], height[i + 2])

        if height[i] < max(left, right): continue

        res += height[i] - max(left, right)

    print(f'#{test_case} {res}')
