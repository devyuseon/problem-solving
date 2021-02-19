import sys
import heapq

def binary_search(start, end, list, target, result):
    if start > end:
        return
    
    mid = ( start + end ) // 2

    if list[mid] == target:
        heapq.heappush(result, target)
    if list[mid] > target:
        end = mid - 1
        binary_search(start, end, list, target, result)
    if list[mid] < target:
        start = mid + 1
        binary_search(start, end, list, target, result)

result = []
hear = []

N, M = map(int, input().split())

for _ in range(N):
    hear.append(sys.stdin.readline().rstrip())

l = len(hear)
hear.sort()

for _ in range(M):
    see = sys.stdin.readline().rstrip()
    binary_search(0, l-1, hear, see, result)

print(len(result))
while result:
    print(heapq.heappop(result))