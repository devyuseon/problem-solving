import sys
import heapq

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = sys.maxsize


def dijkstra():
    Q = []
    heapq.heappush(Q, (matrix[0][0], 0, 0))
    dist[0][0] = 0

    while Q:
        cost, x, y = heapq.heappop(Q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {dist[x][y]}')
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                alt = cost + matrix[nx][ny]

                if alt < dist[nx][ny]:
                    dist[nx][ny] = alt
                    heapq.heappush(Q, (alt, nx, ny))


cnt = 1
while True:
    n = int(input())
    if n == 0: break

    matrix = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    cnt += 1
