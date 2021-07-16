import sys
import heapq

N = int(input())
weight = [int(sys.stdin.readline()) for _ in range(N)]
weight.sort(reverse = True) # 내림차순으로 정렬

result = []

for i in range(N):
    heapq.heappush(result, -weight[i] * (i + 1))

print(-heapq.heappop(result))
# print(-result[0]) 이 더 빠를듯