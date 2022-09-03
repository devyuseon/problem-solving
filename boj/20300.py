# pypy3 115336kb / 144ms

from collections import deque

n = int(input())
nums = deque(sorted(list(map(int, input().split()))))
res = 0

if n % 2 != 0:
    res = nums.pop()
    
while nums:
    res = max(res, nums.pop() + nums.popleft())
    
print(res)