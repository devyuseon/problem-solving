H, W = tuple(map(int, input().split()))
drops = list(map(int, input().split()))

left, right = 0, W - 1
max_left = drops[left]
max_right = drops[right]

result = 0

while left < right:
    max_left = max(max_left, drops[left])
    max_right = max(max_right, drops[right])
    
    if max_left >= max_right:
        result += max_right - drops[right]
        right -= 1
    if max_left < max_right:
        result += max_left - drops[left]
        left += 1
        
print(result)