# 5256. [파이썬 S/W 문제해결 최적화] 2일차 - 이항계수

import sys
sys.stdin = open("SWEA\input.txt", "r")

def solution(n):
    for i in range(2, n + 1):
        tmp = [0] * (i + 1)
        tmp[0] = 1; tmp[i] = 1
        for j in range(1, i):
            tmp[j] = dp[i - 1][j - 1] + dp[i - 1][j]
        dp.append(tmp)

T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    dp = [[1], [1, 1]]
    solution(n)
    print(f'#{test_case} {dp.pop()[b]}')