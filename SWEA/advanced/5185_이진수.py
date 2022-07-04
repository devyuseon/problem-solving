# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, num = input().split()
    num = bin(int(num, 16))[2:]
    if len(num) < int(n) * 4:
        num = '0' + num
    
    print(f'#{test_case} {num}')