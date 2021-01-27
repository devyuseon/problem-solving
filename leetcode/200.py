from typing import List

class Solution:
    grid: List[List[str]]

    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i:int, j:int):
            # 육지가 아닌 경우
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                    return
        
            grid[i][j] = "discovered" # 방문함
            # 육지 인 경우 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count