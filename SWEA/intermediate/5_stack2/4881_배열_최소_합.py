import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())

def dfs(N, i, SUM):
    global MIN
    
    if N == i:
        if SUM < MIN:
            MIN = SUM
    
    if MIN < SUM:
        return
    else:
        for j in range(N):
            if visited[j] == False:
                visited[j] = True
                dfs(N, i + 1, SUM + nums[i][j])
                visited[j] = False

for test_case in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    MIN = 10 * N
    dfs(N, 0, 0)
    print(f'#{test_case} {MIN}')
    