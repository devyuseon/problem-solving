n = int(input())
nums = list(map(int, input().split()))
stack = []
res = [-1 for _ in range(n)]

for i, n in enumerate(nums):
    while stack and nums[stack[-1]] < n:
        j = stack.pop()
        res[j] = n
    stack.append(i)

print(*res)