# pypy3 116496kb / 228ms

def is_contain(n, k):
    n = str(n)
    if len(n) == 1:
        n = '0' + n
    if str(k) in n:
        return True
    return False

n, k = map(int, input().split())
cnt = 0
for i in range(n + 1):
    for j in range(60):
        for l in range(60):
            if is_contain(i,k) or is_contain(j,k) or is_contain(l,k):
                cnt += 1
print(cnt)