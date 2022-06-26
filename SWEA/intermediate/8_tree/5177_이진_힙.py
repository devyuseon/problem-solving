import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    node = [0] + list(map(int, input().split()))
    result = 0

    for i in range(1, N+1):
        while node[i//2] > node[i]: 
            node[i//2], node[i] = node[i], node[i//2]
            i //= 2    

    p = N//2   
    while p > 0:
        result += node[p]
        p //= 2

    print(f'#{test_case} {result}')

