# 7차시 2일차 - 이진탐색

import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

def binary_search(start, end, target, depth):
    mid = (start + end) // 2
    
    if target == mid: return depth
    elif target >= start and target < mid:
        return binary_search(start, mid, target, depth + 1)
    elif target > mid and target <= end:
        return binary_search(mid, end, target, depth + 1)

T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    nums = [i for i in range(1, P + 1)]
    A_result, B_result = 0, 0
    A_result += binary_search(1, P, A, 0)
    B_result += binary_search(1, P, B, 0)
    
    result = ''
    if A_result > B_result:
        result = 'B'
    elif A_result < B_result:
        result = 'A'
    else:
        result = 0
        
    print(f'#{test_case} {result}')