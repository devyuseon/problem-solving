import heapq
from typing import List

def largest(nums: List):
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))
    
    max = heapq.heappop(heap)[1]
    print(max, nums.index(max) + 1)

nums = []
for _ in range(0,9):
    nums.append(int(input()))
largest(nums)
    