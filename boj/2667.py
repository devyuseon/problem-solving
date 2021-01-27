from typing import List

def dfs(graph: List[List[int]], N:int, i:int, j:int, count_house: List, count_apart:int):
    # 더이상 집이 아닌 경우 return
    if i < 0 or i >= N or \
        j < 0 or j  >= N or \
            graph[i][j] <= 0:
            return
    
    # 집인 경우
    graph[i][j] = -1 # 구분하기 위함(방문)
    count_house[count_apart] += 1
    dfs(graph, N, i-1, j, count_house, count_apart)
    dfs(graph, N, i, j-1, count_house, count_apart)
    dfs(graph, N, i+1, j, count_house, count_apart)
    dfs(graph, N, i, j+1, count_house, count_apart)


# 입력
N = int(input())
graph = []
for i in range(0, N):
    graph.append((list(map(int, input()))))

count_apart = 0
count_house = [0]

for i in range(0, N):
    for j in range(0, N):
        if graph[i][j] > 0:
            dfs(graph, N, i, j, count_house, count_apart)
            count_apart += 1
            count_house.append(0)

filter(lambda x: x != 0, count_house)
count_house.sort()

# 출력
print(count_apart)
for n in count_house:
    if n != 0:
        print(n)
