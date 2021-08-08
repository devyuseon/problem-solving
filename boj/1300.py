N = int(input())
K = int(input())

low, high = 1, N * N

while low <= high:
    mid = (low + high) // 2
    count = 0

    for i in range(1, N + 1):
        count += min(mid // i, N)
    if count >= K:
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)