# 9차시 1일차 - 구간합

import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    start, end = 1, M
    SUM = sum(nums[:end])
    MIN, MAX = SUM, SUM
    
    for i in range(M, N):
        SUM += nums[i] - nums[i - M]
              
        if SUM < MIN: MIN = SUM
        if SUM >= MAX: MAX = SUM

    print(f'#{test_case} {MAX-MIN}')