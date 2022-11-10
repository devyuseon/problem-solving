import sys

input = sys.stdin.readline

n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]
pillar.sort()
res = 0

max_idx = 0
for i, v in enumerate(pillar):
    l, h = v
    if res < h:
        max_idx, res = i, h

height = pillar[0][1]

for i in range(max_idx):
    res += height * (pillar[i + 1][0] - pillar[i][0])
    if height < pillar[i + 1][1]:
        height = pillar[i + 1][1]

height = pillar[-1][1]

for i in range(n - 1, max_idx, -1):
    res += height * (pillar[i][0] - pillar[i - 1][0])
    if height < pillar[i - 1][1]:
        height = pillar[i - 1][1]

print(res)