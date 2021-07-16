import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jewels = []
bags = []
sum = 0

# jewels는 무게 기준 최소힙
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewels, (M, V))

bags = [int(sys.stdin.readline()) for _ in range(K)]
# 가방은 오름차순 정렬
bags.sort()

possible = []

for bag in bags:
    while jewels and bag >= jewels[0][0]:
        m, v = heapq.heappop(jewels)
        # 담을수 있는 것은 가격 기준 최대힙
        heapq.heappush(possible, -v)
    if possible:
        sum += -heapq.heappop(possible)

print(sum)