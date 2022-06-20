# 5차시 3일차 - 글자수

import sys
from collections import defaultdict
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = set(' '.join(input()).split())
    str2 = input()
    dict = defaultdict(int)
    
    for s in str2:
        if s in str1:
            dict[s] += 1
    
    print(f'#{test_case} {max(dict.values())}')