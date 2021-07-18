import sys
from collections import deque

def add_nums(nums, add):
    tmp = 0

    for i in range(0, len(nums) - 1, 2):
        # 둘 다 양수이거나 음수인 경우 곱해서 더함
        if nums[i] * nums[i + 1] > 0:
            tmp += nums[i] * nums[i + 1]
        else:
            tmp += (nums[i] + nums[i + 1])

    if len(nums) % 2 != 0:
        n = nums.pop()
        if n < 0 and 0 in add:
            n = 0
        tmp += n
    
    return tmp

N = int(input())


result = 0
add = []
nums = []
negative = []
positive = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 or n == 1:
        add.append(n)
    else:
        nums.append(n)

result += sum(add)

# 음수는 오름차순, 양수는 내림차순으로 정렬
for i, n in enumerate(nums):
    if n < 0: negative.append(n)
    else: positive.append(n)

negative.sort()
positive.sort(reverse = True)

result += add_nums(negative, add)
result += add_nums(positive, add)

print(result)