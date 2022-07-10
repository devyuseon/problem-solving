# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

import sys
import heapq
sys.stdin = open("SWEA\input.txt", "r")

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra(a, b):
    Q = [(0, a, b)] # 가중치, 정점
    
    while Q:
        cost, cur_x, cur_y = heapq.heappop(Q)
        
        if dist[cur_x][cur_y] == None:
            dist[cur_x][cur_y] = cost
            
            # 도착점에 도착
            if cur_x == n - 1 and cur_y == n - 1:
                return
            
            for i in range(4):
                x, y = cur_x + dx[i], cur_y + dy[i]
                
                if x >= 0 and x < n and y >= 0 and y < n:
                    tmp = matrix[x][y] - matrix[cur_x][cur_y]
                    if tmp > 0: # 다음 지역이 더 높음
                        heapq.heappush(Q, (cost + 1 + tmp, x, y))
                    else:
                        heapq.heappush(Q, (cost + 1, x, y))
                    
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dist = [[None] * n for _ in range(n)]
    dijkstra(0, 0)
    print(f'#{test_case} {dist[n-1][n-1]}')