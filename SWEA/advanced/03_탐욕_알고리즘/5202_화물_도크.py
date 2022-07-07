# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    works = [tuple(map(int, input().split())) for _ in range(n)] # (시작시간, 종료시간)
    result = []
    
    # 끝나는 시간 기준 내림차순으로 정렬
    works.sort(key = lambda x: x[1], reverse = True)
    result.append(works.pop()) # 첫 작업은 가장 빨리 끝나는 작업으로 할당
    
    while works:
        cur_end = result[-1][1]
        work = works.pop()
        next_start = work[0]
        
        if cur_end <= next_start:
            result.append(work)
    
    print(f'#{test_case} {len(result)}')