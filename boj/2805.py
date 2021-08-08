import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort() # 오름차순 정렬
low = 0
high = trees[len(trees) - 1]

while low <= high:
    mid = (low + high) // 2

    
    slice = [t - mid for t in trees if (t - mid) >= 0]

    # 필요한거보다 많이 자른것. 더 크게 잘라야 나무아낌
    if sum(slice) >= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)