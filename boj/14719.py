H, W = tuple(map(int, input().split()))
drops = list(map(int, input().split()))

sum = 0

for i in range(1, W - 1):
    left_max, right_max = -1, -1
    for j in range(i):
        if drops[j] >= drops[i]:
            left_max = max(left_max, drops[j])
    for k in range(i + 1, W):
        if drops[k] >= drops[i]:
            right_max = max(right_max, drops[k])
    if left_max != -1 and right_max != -1:
        MIN = min(left_max, right_max)
        sum += MIN - drops[i] # 빗물계산
        
print(sum)