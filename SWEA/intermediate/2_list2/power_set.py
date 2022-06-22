# 6차시 2일차 - 부분집합의 합

import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())
nums = [i for i in range(1, 13)]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = []
    
    for i in range(1 << 12): # 1<<12: 부분 집합의 개수
        tmp = []
        for j in range(12):
            if i & (1 << j): # i의 j번째 비트가 1이면 True
                tmp.append(nums[j])
        if sum(tmp) == K and len(tmp) == N:
            result.append(tmp) 
    
    print(f'#{test_case} {len(result)}')    