# 5255. [파이썬 S/W 문제해결 최적화] 2일차 - 타일 붙이기

import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    dp = [1, 3, 6]
    for i in range(3, n):
        dp.append(dp[i - 3] + dp[i - 2] * 2 + dp[i - 1])
    print(f'#{test_case} {dp.pop()}')