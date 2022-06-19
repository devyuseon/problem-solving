# 7차시 1일차 - 전기버스

import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargings = list(map(int, input().split()))
    cur = 0 # 현재 인덱스
    result = 0 # 총 충전 횟수
    
    while cur < N:
        next = cur + K
        if next >= N: break
        if next in chargings:
            cur = next # 이동
            result += 1 # 충전
        else: # 충전기 없음. 중간에 충전해야함
            # cur보단 크고 next보단 작은 수중 chargings에 있어야함
            mid = 0
            for i in reversed(range(cur + 1, next)):
                if i in chargings:
                    mid = i
                    break
            
            if mid != 0:
                cur = mid
                result += 1
            else:
                result = 0
                break
    
    print(f'#{test_case} {result}')