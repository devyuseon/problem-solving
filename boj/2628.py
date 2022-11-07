import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
width = [0] * (w + 1)
height = [0] * (h + 1)
width[0], width[w], height[0], height[h] = 1, 1, 1, 1
res = 0


def solution(k, li):
    tmp = []
    prev = 0
    for i in range(1, k + 1):
        if li[i] == 1:
            tmp.append(i - prev)
            prev = i
    return tmp


for _ in range(n):
    m, k = map(int, input().split())
    if m == 0:
        height[k] = 1
    else:
        width[k] = 1

garo_pcs = solution(w, width)
sero_pcs = solution(h, height)

for i in garo_pcs:
    for j in sero_pcs:
        res = max(res, i * j)

print(res)