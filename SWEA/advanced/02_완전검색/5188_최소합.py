# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

import sys
sys.stdin = open("SWEA\input.txt", "r")

def dfs(x, y, _sum, n):
    global result
    
    if x == n and y == n:
        _sum += matrix[x][y]
        if _sum < result:
            result = _sum
        return
    
    if x > n or x < 0 or \
        y > n or y < 0:
            return
    
    # 우, 하
    dfs(x + 1, y, _sum + matrix[x][y], n)
    dfs(x, y + 1, _sum + matrix[x][y], n)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = 10 * n^2 # 최댓값 설정
    dfs(0, 0, 0, n - 1)
    print(f'#{test_case} {result}')