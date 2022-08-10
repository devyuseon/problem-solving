# pypy3 116896kb / 192ms

n, m = map(int, input().split())

def dfs(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        dfs(s)
        s.pop()

dfs([])