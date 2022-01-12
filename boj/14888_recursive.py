import sys

# +, -, *, /
def dfs(depth: int, nums: list, plus: int, minus: int, multiple: int, divide: int, result: int):
    global MAX, MIN
    
    if depth == len(nums) - 1:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    
    if plus:
        dfs(depth + 1, nums, plus - 1, minus, multiple, divide, result + nums[depth + 1])
    if minus:
        dfs(depth + 1, nums, plus, minus - 1, multiple, divide, result - nums[depth + 1])
    if multiple:
        dfs(depth + 1, nums, plus, minus, multiple - 1, divide, result * nums[depth + 1])
    if divide:
        if result < 0:
            dfs(depth + 1, nums, plus, minus, multiple, divide - 1, (result*(-1) // nums[depth + 1]) * (-1))
        else:
            dfs(depth + 1, nums, plus, minus, multiple, divide - 1, result // nums[depth + 1])


N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

MAX = -sys.maxsize
MIN = sys.maxsize

dfs(0, nums, op[0], op[1], op[2], op[3], nums[0])

print(MAX)
print(MIN)