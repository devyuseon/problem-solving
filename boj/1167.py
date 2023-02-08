import sys
from collections import defaultdict

input = sys.stdin.readline

v = int(input())
graph = defaultdict(list)
max_len, fianl_node = 0, 0
visited = [False for _ in range(v + 1)]

for _ in range(v):
    info = list(map(int, input().split()))
    s = info[0]
    for i in range(1, v + 1, 2):
        if info[i] == -1: break
        e, c = info[i], info[i + 1]
        graph[s].append([e, c])


def dfs(node, cnt):
    global max_len, fianl_node

    visited[node] = True

    if max_len < cnt:
        fianl_node = node
        max_len = cnt

    for u, c in graph[node]:
        if not visited[u]:
            dfs(u, c + cnt)


dfs(1, 0)

max_len = 0
visited = [False for _ in range(v + 1)]

dfs(fianl_node, 0)

print(max_len)