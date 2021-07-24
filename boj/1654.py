import sys

K, N = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]

arr.sort()
result = 0

low = 1
high = arr[len(arr) - 1]

while low <= high:
    mid = ( low + high ) // 2
    slice = [i // mid for i in arr]

    if sum(slice) >= N:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)