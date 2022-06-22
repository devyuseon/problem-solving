# 8차시 1일차 - 숫자 카드

import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, ' '.join(input()).split()))
    nums.sort() # 오름차순 정렬
    count = [0] * (max(nums) + 1)
   
    for n in nums:
       count[n] += 1
    
    cnt = max(count)
    
    card = 0
    for i, n in enumerate(count[::-1]):
        if n == cnt:
            card = max(nums) - i
            break
    
    print(f'#{test_case} {card} {cnt}')
   