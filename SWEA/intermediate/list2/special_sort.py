# 8차시 2일차 - 특별한 정렬

import sys
from collections import deque
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort() # 오름차순 정렬
    nums = deque(nums)
    cnt = 5
    
    print(f'#{test_case}', end = '')
    while nums and cnt > 0:
        print(f' {nums.pop()}', end = '')
        print(f' {nums.popleft()}', end = '')
        cnt -= 1
    print()