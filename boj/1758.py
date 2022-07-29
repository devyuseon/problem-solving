# pypy3 115804kb / 136ms

import sys
input = sys.stdin.readline

n = int(input())
tip = [int(input()) for i in range(n)]
tip.sort(reverse = True)
result = 0

for i, t in enumerate(tip):
    tmp = t - i
    if tmp > 0:
        result += tmp
print(result)