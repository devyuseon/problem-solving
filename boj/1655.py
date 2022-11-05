import sys
import heapq
input = sys.stdin.readline


n = int(input())
max_h, min_h = [], []

for _ in range(n):
    m = int(input())

    if len(max_h) != len(min_h):
        heapq.heappush(min_h, m)
    else:
        heapq.heappush(max_h, -m)

    if max_h and min_h and max_h[0] * -1 > min_h[0]:
        max_v = heapq.heappop(max_h) * -1
        min_v = heapq.heappop(min_h)

        heapq.heappush(max_h, min_v * -1)
        heapq.heappush(min_h, max_v)

    print(max_h[0] * -1)