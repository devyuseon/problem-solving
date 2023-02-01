import sys
input = sys.stdin.readline

n, h = map(int, input().split())
length = [0 for i in range(h)]

next = True # 석순
for _ in range(n):
    s = int(input())
    if next:
        length[s] -= 1
    else:
        length[h - s] += 1
    next = not next

length[0] = n // 2
for i in range(1, h):
    length[i] += length[i - 1]

_min = min(length[1:])
print(_min, length.count(_min))