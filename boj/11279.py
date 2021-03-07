import heapq
from sys import stdin

N = int(stdin.readline().rstrip())
heap = []

for _ in range(N):
    command = int(stdin.readline().rstrip())

    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-command, command))