# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

import sys
sys.stdin = open("SWEA\input.txt", "r")

def find_triplet(cnt, c):
    if cnt[c] == 3:
        return True
    else:
        return False
    
def find_run(cnt, c):
    if 0 < c < 9:
        if cnt[c - 1] and cnt[c + 1]: return True
    if 0 <= c < 8:
        if cnt[c + 1] and cnt[c + 2]: return True
    if 1 < c <= 9:
        if cnt[c - 1] and cnt[c - 2]: return True
    return False
        
    
def baby_gin():
    for i in range(12):
        if i % 2 == 0:
            one[cards[i]] += 1
            if find_run(one, cards[i]) or find_triplet(one, cards[i]):
                return 1
        else:
            two[cards[i]] += 1
            if find_run(two, cards[i]) or find_triplet(two, cards[i]):
                return 2
    return 0
    
T = int(input())
for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))
    one, two = [0] * 10, [0] * 10
    print(f'#{test_case} {baby_gin()}')