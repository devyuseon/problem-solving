import collections
import sys
from collections import defaultdict

def find_most_have(nums: defaultdict):
    max_num = 0
    most_have_list = []
    # 가장 많이 가진 정수의 갯수를 구함
    for v in nums.values():
        if v > max_num:
            max_num = v
    
    # max_num개를 가진 정수 리스트 구함
    for k, v in nums.items():
        if nums[k] == max_num:
            most_have_list.append(k)
    
    return min(most_have_list)

N = int(input())
nums = defaultdict(int)
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    nums[num] += 1

print(find_most_have(nums))