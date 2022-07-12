# 5254. [파이썬 S/W 문제해결 최적화] 1일차 - 부분 문자열
# https://todaycode.tistory.com/104

import sys
sys.stdin = open("SWEA\input.txt", "r")

def get_lcp(s1, s2):
    s = min(len(s1), len(s2))
    cnt = 0
    
    for i in range(s):
        if s1[i] != s2[i]:
            break
        cnt += 1
    
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    n, string = input().split()
    n = int(n)
    leng = len(string)
    lcp = [0] * leng
    suffix = []
    result = ''
    
    # 접미사 배열
    for i in range(0, leng):
        suffix.append(string[i:leng])
    
    # 접미사 배열 사전순 정렬
    suffix.sort()
    
    # lcp 배열 구하기
    for i in range(0, leng):
        lcp[i] = get_lcp(suffix[i - 1], suffix[i])
    
    cnt = 0
    for i in range(0, leng):
        cnt += len(suffix[i]) - lcp[i] # lcp 배열을 이용해 부분 문자열의 중복 제거
        
        if cnt >= n: # n번째를 구할 수 있는 범위 안에 들어옴
            result = suffix[i][0 : len(suffix[i]) - (cnt - n)]
            break            
    
    print(f'#{test_case} {result[0]} {len(result)}')