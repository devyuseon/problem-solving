# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
# https://kimi10.tistory.com/4 나 왜 실수 -> 이진수 모름..?
import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = float(input())
    result = ''
    cnt = 0
    flag = True
    
    while True:
        next = n * 2
        result += str(int(next))
        n = next - int(next) # 정수 부분 버림
        cnt += 1
        if n == 0.0:
            break
        if cnt > 13:
            flag = False
            break
        
    print(f'#{test_case} ', end = '')
    if flag == False:
        print('overflow')
    else:
        print(result)