# Counting sort 딕셔너리 이용
import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(len(arr)):
    for _ in range(arr[i]):
        print(i)

"""
import sys

def quick_sort(arr: list, start: int, end: int):
    part2 = partition(arr, start, end)

    # 왼쪽
    if 1 < part2 - start:
        quick_sort(arr, start, part2 - 1)
    # 오른쪽
    if part2 < end:
        quick_sort(arr, part2, end)

def partition(arr: list, start: int, end: int):
    pivot = arr[(start + end) // 2]
    while start <= end:
        while arr[start] < pivot: start += 1
        while arr[end] > pivot: end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return start


N = int(input())
arr = [int(sys.stdin.readline().strip()) for x in range(N)]
quick_sort(arr, 0, len(arr) - 1)
for x in arr: sys.stdout.write(str(x) + "\n")
"""