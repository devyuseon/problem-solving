import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())

# 0은 통로, 1은 벽, 2는 출발, 3은 도착
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    
    start_x, start_y = 0, 0 # 출발지점 좌표
    # 출발 지점 찾기
    for r, line in enumerate(matrix):
        for c, point in enumerate(line):
            if point == 2:
                start_x, start_y = r, c
    
    stack = [(start_x, start_y)] # 백트래킹 스택
    visited = [[False] * N for _ in range(N)] # 방문 지점 표시하는 리스트
    visited[start_x][start_y] = True # 시작 지점 방문
    result = 0 # 결과
    
    while stack:
        cur_x, cur_y = stack.pop() # x, y좌표
        
        # 인접한 노드들 스택에 담고 방문 표시
        for i in range(4):
            x, y = cur_x + dx[i], cur_y + dy[i]
            
            if x >= 0 and x < N and \
                y >= 0 and y < N:
                    if matrix[x][y] == 3:
                        result = 1
                        break
                    if not visited[x][y] and matrix[x][y] == 0:
                        stack.append((x, y))
                        visited[x][y] = True
    
    print(f'#{test_case} {result}')