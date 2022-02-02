import sys
import collections
input = sys.stdin.readline
graph = collections.defaultdict(list)

def dfs(v, visited = []):
    visited.append(v)
    for w in sorted(graph[v]):
        if not w in visited:
            visited = dfs(w, visited)
    return visited
    
def bfs(v, visited = []):
    visited.append(v)
    queue = collections.deque()
    queue.append(v)
    while queue:
        w = queue.popleft()
        for w in sorted(graph[w]):
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

v, e, start = map(int, input().split())

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(*dfs(start))
print(*bfs(start))