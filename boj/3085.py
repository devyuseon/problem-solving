from sys import stdin

n = int(input())
board = []
max_candy = 0
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    line = " ".join(stdin.readline()).split()
    board.append(line)

# diff(다른 사탕 등장)가 1 초과가 되면 dfs 탐색 중단
def dfs(x, y, candy, diff, count, visited):
    global max_candy
    
    if x > len(board) - 1 or x < 0 or \
        y > len(board) -1 or y < 0 or \
            visited[x][y] == True:
            return
    
    if board[x][y] != candy:
        if diff == 0:
            diff += 1
        else:
            max_candy = max(max_candy, count)
            print(visited)
            return
    
    visited[x][y] = True
    
    dfs(x + 1, y, candy, diff, count + 1, visited)
    dfs(x - 1, y, candy, diff, count + 1, visited)
    
for i in range(n):
    for j in range(n):
        dfs(i, j, board[i][j], 0, 0, visited)
        
print(max_candy)