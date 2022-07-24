import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [i for i in range(1, n + 1)]
result = []
idx = 0

for _ in range(n):
    idx += k - 1
    if idx >= len(li):
        idx %= len(li)
    result.append(str(li.pop(idx)))

print('<', ', '.join(result), '>', sep = '')