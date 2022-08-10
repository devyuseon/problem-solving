# pypy3 113112kb / 108ms

n, m = map(int, input().split())

def dfs(s, l):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(l, n + 1):
        if i in s:
            continue
        s.append(i)
        dfs(s, i)
        s.pop()

dfs([], 1)