import sys
input = sys.stdin.readline
           
n, k = map(int, input().split())
values = [int(input().strip()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    for j in range(values[i], k + 1):
        dp[j] += dp[j - values[i]]

print(dp[k])