# 80퍼 틀림......

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                
city = list(map(int, input().split()))
flag = True

for i in range(0, m - 1):
    if not graph[city[i] - 1][city[i + 1] - 1]:
        flag = False
        break
    
if flag: print("YES")
else: print("NO")