# pypy3 121884kb / 248ms

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    m = int(input())
    if m != 0:
        heapq.heappush(heap, (abs(m), m))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)