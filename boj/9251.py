# pypy3 123084kb / 160ms

str1, str2 = input(), input()
h, w = len(str1), len(str2)
dp = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])