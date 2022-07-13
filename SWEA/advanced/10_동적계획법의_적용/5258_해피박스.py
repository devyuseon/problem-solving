# 5258. [파이썬 S/W 문제해결 최적화] 3일차 - 해피박스

import sys
sys.stdin = open("SWEA\input.txt", "r")

def solution(n, m): # 박스의 크기, 상품의 개수
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if items[i][0] > j: # 상품의 크기가 담을 수 있는 크기보다 크면
                dp[i][j] = dp[i - 1][j] # 그 전 행의 값을 그대로 가져옴
            else:
                dp[i][j] = max(dp[i - 1][j - items[i][0]] + items[i][1], dp[i - 1][j])
    return dp[m][n]
                
    

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    items = [0]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m):
        s, p = map(int, input().split()) # 크기, 가격
        items.append((s, p))

    print(f'#{test_case} {solution(n, m)}')