import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = set(map(int, input().split()))
given = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n + 3)]

for num in given:
    if num not in sleep:
        for i in range(num, n + 3, num):
            if i not in sleep:
                prefix_sum[i] = 1

for i in range(1, n + 3):
    prefix_sum[i] += prefix_sum[i - 1]

for _ in range(m):
    s, e = map(int, input().split())
    print(e - s + 1 - prefix_sum[e] + prefix_sum[s - 1])