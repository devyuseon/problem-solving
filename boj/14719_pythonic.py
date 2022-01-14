H, W = tuple(map(int, input().split()))
drops = list(map(int, input().split()))

result = 0

for i in range(1, W - 1):
    max_left = max(drops[:i + 1])
    max_right = max(drops[i:])
    MIN = min(max_left, max_right)
    result += abs(drops[i] - MIN)
        
print(result)