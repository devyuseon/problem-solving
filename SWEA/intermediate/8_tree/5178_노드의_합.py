import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # N: 노드개수, M: 리드노프의개수, L: 출력할 노드번호
    N, M, L = map(int, input().split())
    graph = [0] * (N + 1)
    for i in range(M):
        n, v = map(int, input().split())
        graph[n] = v
        
    for i in range(N, 0, -1):
        if i // 2 > 0:
            graph[i // 2] += graph[i]
    
    print(f'#{test_case} {graph[L]}')