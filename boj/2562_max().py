nums = []
for _ in range(0,9):
    nums.append(int(input()))

print(max(nums), nums.index(max(nums)) + 1)