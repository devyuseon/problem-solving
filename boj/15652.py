# pypy3 118144kb / 204ms

n, m = map(int, input().split())

def dfs(s, l):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(l, n + 1):
        s.append(i)
        dfs(s, i)
        s.pop()

dfs([], 1)