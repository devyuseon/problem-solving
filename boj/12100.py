import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def move(board, dir):
    if dir == 0:  # right
        for i in range(n):
            pointer = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:  # 포인터가 가리키는 수가 0
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:  # 포인터와 현재위치 수가 같을 때
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:  # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                        pointer -= 1
                        board[i][pointer] = tmp
    elif dir == 1:  # left
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
    elif dir == 2:  # up
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        board[pointer][j] = tmp
    else:
        for j in range(n): # down
            pointer = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    return board


def dfs(board, cnt):
    global ans

    if cnt == 5:
        ans = max(ans, max(map(max, board)))
        return

    for i in range(4):
        dfs(move(deepcopy(board), i), cnt + 1)


dfs(board, 0)
print(ans)
