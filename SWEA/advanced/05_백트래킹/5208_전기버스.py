# [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

import sys
sys.stdin = open("SWEA\input.txt", "r")

def dfs(cur, cnt):
    global MIN
    
    if cnt >= MIN: return
    
    # 도착
    if cur >= n - 1:
        if cnt < MIN:
            MIN = cnt
        return
    
    for i in range(chargings[cur]):
        dfs(cur + i + 1, cnt + 1)

T = int(input())
for test_case in range(1, T + 1):
    n, *chargings = list(map(int, input().split()))
    MIN = 987654321
    dfs(0, -1)
    print(f'#{test_case} {MIN}')