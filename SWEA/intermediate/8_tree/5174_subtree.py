import sys
sys.stdin = open("SWEA\input.txt", "r")

def subtree(root):
    global count
    count += 1

    for i in graph[int(root)]:
        if i:
            subtree(i)

    return count


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())

    nodes = list(input().split())
    graph = [[] for _ in range(E + 2)]
    for t in range(0, len(nodes), 2):
        graph[int(nodes[t])].append(nodes[t + 1])
    count = 0
    
    print(f'{test_case} {subtree(N)}')