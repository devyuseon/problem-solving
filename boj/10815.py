# pypy3 224524kb / 616ms

import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for n in nums:
    if n in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')