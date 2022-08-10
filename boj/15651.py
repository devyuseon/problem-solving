# pypy3 124280kb / 720ms

n, m = map(int, input().split())

def dfs(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        s.append(i)
        dfs(s)
        s.pop()

dfs([])