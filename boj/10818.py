"""
N = int(input())
nums = list(map(int,input().split()))
print(min(nums), end=" ")
print(max(nums))
"""

import sys

N = int(input())

nums = map(int,sys.stdin.readline().split())

max = -sys.maxsize
min = sys.maxsize

for n in nums:
    if n > max:
        max = n
    if n < min:
        min = n

print(min, max)