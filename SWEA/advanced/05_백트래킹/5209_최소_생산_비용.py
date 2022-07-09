# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

import sys
sys.stdin = open("SWEA\input.txt", "r")

def dfs(i, tmp): # i: 행
    global result
    
    if tmp >= result: return
    
    if i == n:
        result = min(tmp, result)
        return
    
    for j in range(n): # j는 열
        if not visited[j]:
            visited[j] = True
            dfs(i + 1, tmp + cost[i][j]) # 행을 증가시킴
            visited[j] = False
    
    
    

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    result = 15 * 15 * 99
    visited = [False] * n # 열 방문 여부
    
    dfs(0,0)
    
    print(f'#{test_case} {result}')