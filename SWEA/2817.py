T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res = 0

    def dfs(_sum, idx):
        global res

        if _sum == k:
            res += 1
            return

        if _sum > k:
            return

        for i in range(idx, len(nums)):
            dfs(_sum + nums[i], i + 1)

    dfs(0, 0)

    print(f'#{test_case} {res}')