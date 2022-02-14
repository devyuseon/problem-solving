from collections import deque
MAX = 10 ** 5

def bfs(n, k):
        
    Q = deque([(n, 0)])
    visited = [0] * (MAX + 1)
    
    while Q:
        cur, time = Q.popleft()
        if cur == k:
            print(time)
            break            
        
        for nx, val in ([cur * 2, 0], [cur - 1, 1], [cur + 1, 1]):
            if 0 <= nx <= MAX and not visited[nx]:
                Q.append((nx, time + val))
                visited[cur] = True

dist = [0] * (MAX + 1)
n, k = map(int, input().split())
bfs(n, k)