# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

import sys
sys.stdin = open("SWEA\input.txt", "r")

def binary_search(target):
    start, end = 0, n - 1
    check = ''
    
    while start <= end:    
        mid = (start + end) // 2
        
        if target == a[mid]:
            return True
        if target < a[mid]: # 타겟이 왼쪽에있음
            if check == 'left':
                break
            check = 'left'
            end = mid - 1
        if target > a[mid]:
            if check == 'right':
                break
            check = 'right'
            start = mid + 1
    return False

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        if binary_search(i):
            cnt += 1
    
    print(f'#{test_case} {cnt}')