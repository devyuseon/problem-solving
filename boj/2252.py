import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
graph = collections.defaultdict(list)
indegree = [0] * (n + 1) # 진입 차수 테이블

result = []
Q = collections.deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입 차수 증가
    
# 초기에 진입 차수 0인 노드들 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        Q.append(i)
            
while Q:
    node = Q.popleft()
        # 꺼낸 원소는 위상 정렬 값에 append
    result.append(node)
        # 꺼낸 노드와 연결된 노드들 탐색
    for v in graph[node]:
        # node 제거 -> 연결된 노드들 간선 -1
        indegree[v] -= 1 
        # 진입간선 0인 노드들 큐에 추가
        if indegree[v] == 0:
            Q.append(v)

print(' '.join(map(str, result)))