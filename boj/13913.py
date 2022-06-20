from collections import deque
from collections import defaultdict
MAX = 10 ** 5
trace = defaultdict(int)

def bfs(n, k):
        
    Q = deque([(n, n, 0)])
    visited = [0] * (MAX + 1)
    
    while Q:
        cur, prev, time = Q.popleft()
        trace[cur] = prev
        if cur == k:
            print(time)
            break            
        
        for nx in (cur - 1, cur + 1, cur * 2):
            if 0 <= nx <= MAX and not visited[nx]:
                Q.append((nx, cur, time + 1))
                visited[cur] = True

dist = [0] * (MAX + 1)
n, k = map(int, input().split())
bfs(n, k)
result = deque([k])
to = k

while True:
    to = trace[to]
    result.appendleft(to)
    if to == n:
        break
print(*result)