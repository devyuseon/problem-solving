# 4차시 3일차 - 회문

import sys

sys.stdin = open("SWEA\input.txt", "r")

def find_palindrome(arr, N, M):
    # row
    for r in range(N):
        for i in range(N - M + 1):
            tmp = arr[r][i : i + M]
            if tmp == tmp[::-1]:
                return ''.join(map(str, tmp))
    # col
    for r in range(N - M + 1):
        for c in range(N):
            tmp = ''
            for i in range(M):
                tmp += arr[r + i][c]
            if tmp == tmp[::-1]:
                return ''.join(map(str, tmp))
            
    
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    
    print(f'#{test_case} ' , end='')
    print(find_palindrome(arr, N, M))
            
    