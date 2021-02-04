from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        traced = set()

        def dfs(i):
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            visited.add(i)

            return True
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
        
