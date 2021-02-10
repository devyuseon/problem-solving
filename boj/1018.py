import sys

N, M = map(int, input().split())
board = []
result = sys.maxsize

for i in range(N):
    board.append(sys.stdin.readline().rstrip())

for x in range(N - 8 + 1):
    for y in range(M - 8 + 1):
        W_start = 0
        B_start = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if i%2 == 0 and j%2 == 0: # 짝수 행, 짝수 열
                    if board[i][j] != "W": W_start += 1
                    if board[i][j] != "B": B_start += 1
                if i%2 == 0 and j%2 != 0: # 짝수 행, 홀수 열
                    if board[i][j] != "B": W_start += 1
                    if board[i][j] != "W": B_start += 1
                if i%2 != 0 and j%2 == 0: # 홀수 행, 짝수 열
                    if board[i][j] != "B": W_start += 1
                    if board[i][j] != "W": B_start += 1
                if i%2 != 0 and j%2 != 0: # 홀수 행, 홀수 열
                    if board[i][j] != "W": W_start += 1
                    if board[i][j] != "B": B_start += 1
        result = min(result, W_start, B_start)

print(result)          