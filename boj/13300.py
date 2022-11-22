import sys
input = sys.stdin.readline

n, k = map(int, input().split())
male = [0] * 7
female = [0] * 7
res = 0

for _ in range(n):
    s, y = map(int, input().split())
    if s == 0:
        female[y] += 1
    else:
        male[y] += 1

for i in range(1, 7):
    if male[i] > 0:
        res += male[i] // k
        if male[i] % k != 0:
            res += 1
    if female[i] > 0:
        res += female[i] // k
        if female[i] % k != 0:
            res += 1

print(res)