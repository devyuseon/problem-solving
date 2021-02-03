from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            result.append(a)

        dfs('JFK')
        return result[::-1]