from collections import defaultdict
from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 큐 변수 (소요시간, 정점, 경유지횟수)
        k = 0
        Q = [(0, src, K)]

        while Q:
            price, node , k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        
        return -1
