import sys
input = sys.stdin.readline

def dfs(houses: list[list[int]], N: int, i: int, j: int, count_house: list, count_apart: int):
    # 집이 아닌 경우
    if i < 0 or i >= N or \
        j < 0 or j  >= N or \
            houses[i][j] <= 0:
            return
    
    # 집인 경우
    houses[i][j] = -1 # 방문 표시
    count_house[count_apart] += 1
    # 위
    dfs(houses, N, i, j - 1, count_house, count_apart)
    # 아래
    dfs(houses, N, i, j + 1, count_house, count_apart)
    # 왼
    dfs(houses, N, i - 1, j, count_house, count_apart)
    # 오
    dfs(houses, N, i + 1, j, count_house, count_apart)
    
N = int(input())
houses = [list(map(int, input().strip())) for _ in range(N)]

count_house = [0]
count_apart = 0

for i in range(N):
    for j in range(N):
        if houses[i][j] > 0:
            dfs(houses, N, i, j, count_house, count_apart)
            count_apart += 1
            count_house.append(0)

count_house.sort()
print(count_apart)
for i in count_house: 
    if i != 0: print(i)