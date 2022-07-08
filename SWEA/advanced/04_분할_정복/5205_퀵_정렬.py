# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

import sys
sys.stdin = open("SWEA\input.txt", "r")
        
def quick_sort(start, end):
    # start와 end 사이에서 파티션 나누고
    # 나눈 파티션의 오른쪽 첫번째 인덱스 받아옴
    right = partition(start, end)
    
    # start와 오른쪽 파티션 첫번째 값이 같으면
    # 정렬 X
    if 1 < right - start: # 오른쪽 파티션 정렬
        quick_sort(start, right - 1)
    if right < end: # 왼쪽 파티션 정렬
        quick_sort(right, end)
    
def partition(start, end):
    pivot = nums[(start + end) // 2]
    while start <= end:
        # 왼쪽 - 피봇보다 작으면 넘어감
        while nums[start] < pivot: start += 1
        # 오른쪽 - 피봇보다 크면 넘어감
        while nums[end] > pivot: end -= 1
        # 왼쪽에서 피봇보다 큰값, 오른쪽에서 피봇보다 작은값
        # 발견하면 둘이 swap
        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    return start # 새로 나눌 오른쪽 파티션의 첫번째 배열방 인덱스
            

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(0, n - 1)
    print(f'#{test_case} {nums[n//2]}')