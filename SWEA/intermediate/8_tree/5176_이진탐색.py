import sys
sys.stdin = open("SWEA\input.txt", "r")

def solution(n):
    global num
    if n <= N:
        solution(n * 2)
        graph[n] = num
        num += 1
        solution(n * 2 + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    graph = [0 for i in range(N + 1)]
    num = 1
    solution(1)
                        
    print(f'#{test_case} {graph[1]} {graph[N // 2]}')