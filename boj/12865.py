# pypy3 193672kb / 392ms

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)] # 가치, 무게
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n): # items 무게
    for j in range(1, k + 1): # 배낭이 담을 수 있는 무게
        w = items[i][0]
        v = items[i][1]

        if j < w: # 전열 그대로 내려옴
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v) # 담음, 안담음

print(dp[n - 1][k])