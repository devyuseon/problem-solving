import sys
input = sys.stdin.readline

n = int(input())
works = [[0, 0]]
works.extend([list(map(int, input().split())) for _ in range(n)])
dp = [0 for _ in range(n + 2)]

for i in range(2, n + 2):
    for j in range(1, i):
        if j + works[j][0] <= i:
            dp[i] = max(dp[i], dp[j] + works[j][1])

print(dp[-1])