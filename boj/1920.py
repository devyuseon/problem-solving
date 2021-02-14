import sys
from typing import List

def binary_search(start: int, end: int, A: List, target: int, result: List):
    mid = (start + end) // 2

    # 종료 조건
    if end < start: # not found
        result.append(0)
        return

    if A[mid] == target: # found
        result.append(1)
        return

    if target < A[mid]:
        end = mid - 1
        return binary_search(start, end, A, target, result)

    if A[mid] < target:
        start = mid + 1
        return binary_search(start, end, A, target, result)



N = int(input())
list1 = list(map(int,sys.stdin.readline().rstrip().split()))
M = int(input())
list2 = list(map(int,sys.stdin.readline().rstrip().split()))

result = []
list1.sort()

for n in list2:
    binary_search(0, N-1, list1, n, result)

for n in result:
    print(n)