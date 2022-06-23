import sys
from collections import deque
sys.stdin = open("SWEA\input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)] # 방문 표시, 거리 측정
    start_x, start_y = 0, 0 # 출발지점
    Q = deque()
    result = 0
    
    # 출발 지점 찾기
    for i, row in enumerate(maze):
        for j, point in enumerate(row):
            if point == 2:
                start_x, start_y = i, j
          
    Q.append((start_x, start_y)) # 시작 지점 큐에 삽입
    
    while Q:
        cur_x, cur_y = Q.popleft()
        
        for i in range(4):
            x, y = cur_x + dx[i], cur_y + dy[i]
            
            if x >= 0 and x < N and \
                y >= 0 and y < N:
                    if maze[x][y] == 3: # 도착
                        result = visited[cur_x][cur_y]
                        break
                    # 방문 하지 않았고, 갈 수 있는 길일때(벽 아닐때)
                    if visited[x][y] == 0 and maze[x][y] == 0:
                        Q.append((x, y)) # 큐에 삽입
                        # 방문, 이전 지점에 +1 해서 경로 구함
                        visited[x][y] = visited[cur_x][cur_y] + 1
                        
    print(f'#{test_case} {result}')