import sys
import collections
import heapq
input = sys.stdin.readline

def dijkstra(start):
    # (소요시간, 정점)
    Q = [(0, start)]

    while Q:
        # 소요시간 가장 적은것 pop, Q최소힙
        time, node = heapq.heappop(Q)
        # 해당 노드에 처음 방문 할 때에만
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

# ------- 입력 받기 시작 ------
N = int(input())
M = int(input())

graph = collections.defaultdict(list)
for _ in range(M):
    # 출발, 도착, 버스비용
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
# ------- 입력 받기 끝 ------

dist = collections.defaultdict(int) # 거리
dijkstra(start)

print(dist[end])