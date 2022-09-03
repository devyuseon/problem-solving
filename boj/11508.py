# pypy3 116532kb / 152ms

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse = True)
res = 0
for i in range(n):
    if i % 3 != 2:
        res += nums[i] 
print(res)