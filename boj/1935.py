# pypy3 114276kb / 140ms

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cal = ' '.join(input()).split()[::-1]
match = defaultdict()
for i in range(n):
    v = int(input())
    match[chr(i + 65)] = v

stack = [match[cal.pop()]]
res = 0
while stack and cal:
    v = cal.pop()
    if v.isalpha(): # 알파벳이면
        stack.append(match[v])
    else:
        v2, v1 = stack.pop(), stack.pop()
        if v == '/':
            stack.append(v1 / v2)
        elif v == '*':
            stack.append(v1 * v2)
        elif v == '+':
            stack.append(v1 + v2)
        elif v == '-':
            stack.append(v1 - v2)

print('%0.2f'% stack[-1])