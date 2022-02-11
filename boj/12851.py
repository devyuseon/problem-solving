from collections import deque    
MAX = 10 ** 5

def bfs(n, k):
    Q = deque([(n, 0)])
    visited = [0] * (MAX + 1)
    count = 0
    min_time = -1
    
    while Q:
        cur, dist = Q.popleft()
        visited[cur] = True
        if cur == k:
            if count == 0:
                min_time = dist
                count += 1
            else:
                if min_time == dist:
                    count += 1            
        
        for nx in (cur - 1, cur + 1, cur * 2):
            if 0 <= nx <= MAX and not visited[nx]:
                Q.append((nx, dist + 1))
    return min_time, count
    
n, k = map(int, input().split())
for i in bfs(n, k): print(i)