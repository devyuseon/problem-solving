import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 부모
rank = [0 for i in range(n + 1)]  # 트리의 깊이


def union(x, y):
    x = find(a)
    y = find(b)

    # 트리의 레벨이 낮은 쪽이 큰쪽 밑으로 붙도록 해 최적화
    if x != y:
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[x] = y
            rank[y] += 1  # x 부모 밑에 y가 들어가므로 y의 rank 증가


def find(x):
    # 루트 노드 찾을때까지
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    if cal == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")