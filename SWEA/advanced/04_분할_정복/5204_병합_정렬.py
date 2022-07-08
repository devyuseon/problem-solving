# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

import sys
sys.stdin = open("SWEA\input.txt", "r")

def divide(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left = divide(li[:mid])
    right = divide(li[mid:])
    return merge(left, right)

def merge(left, right):
    global cnt
    
    merged = []
    l, r = 0, 0
    n, m = len(left), len(right)
    
    if left[-1] > right[-1]:
        cnt += 1
    
    while l < n and r < m:
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    
    while l < n: # 왼쪽배열이 남음
        merged.append(left[l])
        l += 1
    while r < m: # 오른쪽 배열이 남음
        merged.append(right[r])
        r += 1
        
    return merged
        
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    print(f'#{test_case} {divide(nums)[n//2]} {cnt}')