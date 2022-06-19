# 5차시 2일차 - 색칠하기

import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    
    N = int(input())
    matrix = [[''] * 10 for _ in range(10)]
    result = 0
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 1: # red
                    matrix[i][j] += 'R'
                else: # blue
                    matrix[i][j] += 'B'
    
    for i in range(10):
        for j in range(10):
            if 'R' in matrix[i][j] and 'B' in matrix[i][j]:
                result += 1
            
    print(f'#{test_case} {result}')