# pypy3 114280kb / 144ms

import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(root):
    global ans
    
    if None in graph[root]:
        return
    
    if not graph[root]: # 리프노드
        ans += 1
        return

    for i in graph[root]:
            solution(i)

n = int(input())
graph = defaultdict(set)
for i, v in enumerate(list(map(int, input().split()))):
    graph[v].add(i)
delete = int(input())
graph[delete].add(None)
ans = 0

for k, v in graph.items():
    # 지우려는 노드의 부모의 자식이 하나일때
    # 즉 지우려는 노드의 부모의 자식이 지우는 노드뿐일때
    # 그 부모는 리프노드가 되므로 카운트해줌
    # 단, 0을 지울 땐 제외
    if delete in v and len(v) == 1 and k != -1:
        ans += 1
        break
    
solution(-1)
print(ans)