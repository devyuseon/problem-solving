import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]
res = 0


def bound_count(i, j):
    cnt = 0
    for x, y in stars:
        if i <= x <= i + l and j <= y <= j + l: cnt += 1
    return cnt


for s1 in stars:
    for s2 in stars:
        res = max(res, bound_count(s1[0], s2[1]))

print(k - res)