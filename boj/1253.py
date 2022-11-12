n = int(input())
nums = list(map(int, input().split()))
nums.sort()
good = set()


def solution(i, m):
    if m in good:
        return True

    s, e = 0, n - 1
    while s < e:
        if i == s:
            s += 1
            continue
        if i == e:
            e -= 1
            continue

        tmp = nums[s] + nums[e]
        if tmp == m:
            good.add(m)
            return True
        elif tmp < m:
            s += 1
        else:
            e -= 1

    return False


cnt = 0
for i, v in enumerate(nums):
    if solution(i, v):
        cnt += 1

print(cnt)