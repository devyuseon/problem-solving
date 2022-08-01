# pypy3 140716kb / 184ms

n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = [0] * (max(nums) + 1) # 원소 갯수 카운팅

left, right = 0, 0
result = 0

while right < n:
    if cnt[nums[right]] >= k:
        cnt[nums[left]] -= 1
        left += 1
    else:
        cnt[nums[right]] += 1
        right += 1
    result = max(result, right - left)

print(result)