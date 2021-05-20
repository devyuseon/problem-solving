import sys
from typing import List

def dfs(g: List[List[int]], count: int):


T = int(input())
for in T:
    M, N, K =  map(int, input().split())
    g = list()
    while(True):
        tmp = map(int, input().split())

        if len(tmp) == 3: # 배추 위치가 아닐 경우
            M, N, K = tmp
            break

        else:
            dfs(g, 0)

        # dfs 돌기
