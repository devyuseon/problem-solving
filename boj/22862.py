def is_odd(n):
    return n % 2 != 0

n, k = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
ans, odd = 0, 0
if is_odd(nums[right]): odd += 1

while True:
    while right < n - 1:
        if is_odd(nums[right]):
            odd += 1
        right += 1
    
    if left >= n or right >= n: break
    
    ans = max(ans, right - left + 1 - odd)
    if is_odd(nums[left]):
        odd -= 1
    left += 1

print(ans)