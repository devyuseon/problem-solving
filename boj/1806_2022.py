import sys

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# 부분합 만들기
sums = [0] * (N + 1)
for i in range(1, N + 1):
    sums[i] = sums[i - 1] + nums[i - 1]
        
min_length = sys.maxsize
start = 0
end = start + 1

while start != N:
    if sums[end] - sums[start] >= S:
        min_length = min(min_length, end - start)
        start += 1
    else:
        if end != N:
            end += 1
        else:
            start += 1
    
if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)