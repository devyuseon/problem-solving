# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

import sys
from collections import deque
sys.stdin = open("SWEA\input.txt", "r")

def bfs(start):
    # 이걸 평행선 좌표라고 생각하면 쉬움
    Q = deque([(start, 0)])
    visited = set() # 이 문제에서 아마도 가장 중요할..
    visited.add(start)
    
    while Q:
        v, cnt = Q.popleft()
        
        for next in (v + 1, v - 1, v * 2, v - 10):
            if next not in visited and 1 <= next <= 1000000:
                visited.add(next)
                Q.append((next, cnt + 1))
                if next == m:
                    return cnt + 1
                

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print(f'#{test_case} {bfs(n)}')