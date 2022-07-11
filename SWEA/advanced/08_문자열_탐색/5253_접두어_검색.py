# 5253. [파이썬 S/W 문제해결 최적화] 1일차 - 접두어 검색

import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    words = [input().strip() for _ in range(n)]
    cnt = 0
    for _ in range(m):
        string = input().strip()
        for word in words:
            if word.startswith(string):
                cnt += 1
                break
    
    print(f'#{test_case} {cnt}')