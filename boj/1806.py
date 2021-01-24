import sys

N, S = map(int, input().split())
list = list(map(int, input().split()))

# 부분합 못구함
if sum(list) < S:
    print(0)

min_length = sys.maxsize
start = 0
last = start + 1

while(start + min_length != N):
    sub_list = list[start:last+1]
    if sum(sub_list) >= S:
        min_length = min(min_length, len(sub_list))
        start += 1
    else:
        start += 1
        last += 1

print(min_length)
