# 3차시 3일차 - 문자열 비교

import sys
from collections import defaultdict
sys.stdin = open("SWEA\input.txt", "r")

# Boyer-Moore

T = int(input())
for test_case in range(1, T + 1):
    str1, str2 = input(), input()
    skip = defaultdict()
    pat_len = len(str1) # 다른 문자일 경우 스킵 수
    result = 0
    
    for i, s in enumerate(str1):
        skip[s] = pat_len - i - 1
    
    idx = pat_len - 1
    cur = pat_len - 1 # str1 맨 끝
    
    while idx < len(str2):
        # 문자열 일치함
        if cur < 0: # cur이 0보다 작다는 것은
                    # str1을 뒤에서부터 처음까지 다 비교한 뒤라는 것
            result += 1
            break
        # 일치하면 차례대로 검사
        if str1[cur] == str2[idx]:
            idx -= 1
            cur -= 1
        # 일치하지 않으면 해당 문자 패턴에 있는지 검사
        else:
            if str2[idx] in str1:
                idx += skip[str2[idx]]
            else:
                # 일치하는 문자 없으므로 패턴수만큼 건너뜀
                idx += pat_len
            cur = pat_len - 1 # 다시 끝부터 검사
            
    print(f'#{test_case} {result}')