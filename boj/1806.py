import sys

N, S = map(int, input().split())
list = list(map(int, input().split()))

sum_untill_n = [0] * (N+1)
for i in range(1, N + 1):
    sum_untill_n[i] = sum_untill_n[i-1] + list[i-1]

min_length = sys.maxsize
start = 0
end = start + 1

while(start != N):
    if sum_untill_n[end] - sum_untill_n[start] >= S:
        min_length = min(end - start, min_length)
        start += 1

    else:
        if end != N:
            end += 1
        else:
            start += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
