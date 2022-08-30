# https://ahntoday.tistory.com/176

import sys
import heapq
input = sys.stdin.readline

def solution(nums):
    small = []
    big = []
    mid = nums[0]
    result = [mid]
    
    for i, v in enumerate(nums[1:], 1):
        if v > mid:
            heapq.heappush(big, v)
        else:
            heapq.heappush(small, -v)
        
        if i % 2 == 0:
            if len(small) < len(big):
                heapq.heappush(small, -mid)
                mid = heapq.heappop(big)
            elif len(small) > len(big):
                heapq.heappush(big, mid)
                mid = -heapq.heappop(small)
            result.append(mid)
    print(len(result))
    
    for i in range(len(result)):
        if i != 0 and (i + 1) % 10 == 1:
            print()
        print(result[i], end = ' ')
    print()

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    if m % 10 == 0:
        for _ in range(m // 10):
            nums.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            nums.extend(list(map(int, input().rstrip().split())))
    
    solution(nums)