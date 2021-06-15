N = int(input())
nums = list(map(int, input().split()))

nums.sort() # 오름차순으로 정렬
time = 0
for i in range(len(nums)) :
    time += sum(nums[0:i+1])

print(time)