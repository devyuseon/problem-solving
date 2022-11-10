import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
sub_sum = [0] * n
sub_sum[0] = temp[0]

for i in range(1, n):
    if i != 0:
        sub_sum[i] = sub_sum[i - 1] + temp[i]

res = sub_sum[k - 1]
for i in range(k, n):
    tmp = sub_sum[i] - sub_sum[i - k]
    res = max(res, tmp)

print(res)