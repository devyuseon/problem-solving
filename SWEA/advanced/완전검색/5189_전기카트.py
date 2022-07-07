# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
# 혼자 못 품~~~~~~~

import sys
sys.stdin = open("SWEA\input.txt", "r")

def dfs(cur, _sum):
    global result
    
    if _sum < result:
        if False not in visited[1:]: # 모두 한번씩 방문함
            result = min(result, _sum + matrix[cur][0]) # 최솟값 갱신
            return
        else:
            for next in range(1, n):
                # 경곗값이 아니며 방문하지 않았을 때
                if matrix[cur][next] != 0 and visited[next] == False:
                    visited[next] = True
                    dfs(next, _sum + matrix[cur][next])
                    visited[next] = False
    else:
        return

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = 100 * n^2
    
    for i in range(1, n):
        visited = [False] * n
        visited[i] = True # 방문
        # 처음은 1번, 즉 배열에서는 0번에서 시작함.
        # 사무실은 1번, x좌표가 1번(0번)인게 사무실
        # (0, x) 일때 모든 y좌표에 대해 dfs
        dfs(i, matrix[0][i])
    print(f'#{test_case} {result}')