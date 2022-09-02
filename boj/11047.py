# pypy3 114328kb / 312ms

import sys
input = sys.stdin.readline

def find_closer(money):
    for i, v in enumerate(coins):
        if v > money:
            return i - 1
    return len(coins) - 1 # money == 가장 적은 돈

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

while k != 0:
    coin = coins[find_closer(k)]
    while True:
        tmp = k - coin
        if tmp >= 0:
            k -= coin
            cnt += 1
        else: break

print(cnt)