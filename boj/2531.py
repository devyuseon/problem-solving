from collections import defaultdict

n, d, k, c = map(int, input().split())
li = [int(input()) for _ in range(n)]
res = 0

for i in range(n):
    cnt = defaultdict(int)
    cnt[c] += 1
    for j in range(i, i + k):
        j %= n
        cnt[li[j]] += 1
    res = max(res, len(cnt.keys()))

print(res)