from sys import stdin
from collections import defaultdict

N = int(input())
cards_list = map(int,stdin.readline().split())
cards_dict = defaultdict(int)
for n in cards_list:
    cards_dict[n] += 1

M = int(input())
nums = map(int,stdin.readline().split())

for n in nums:
    print(cards_dict[n], end=" ")