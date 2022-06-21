# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

import sys
sys.stdin = open("SWEA\input.txt", "r")

'''
f(1) = 1
f(2) = 3
f(3) = 4
f(4) = 11 # 이건 직접 그림
f(5) = 21
...
f(7) = 85

1 -> 2, 3 -> 4 는 *2 + 1,
2 -> 3, 4 -> 5 는 *2 - 1 인것을 알 수 있음
그럼? f(6)은 43, 이 공식 적용하면 6 -> 7 일때 85가 나옴
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    dp = [1]
    
    for i in range(1, N//10 + 1):
        if i % 2 == 0: # 짝수번째 +
            dp.append(dp[i - 1] * 2 + 1)
        else: # 홀수번째 -
            dp.append(dp[i - 1] * 2 - 1)
    
    print(f'#{test_case} {dp.pop()}')