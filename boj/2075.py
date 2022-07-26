# pypy3 126880kb / 1648ms

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    for i in list(map(int,input().split())):
        heapq.heappush(heap, i) # 최소힙
        if len(heap) > n:
            heapq.heappop(heap)
            
print(min(heap))