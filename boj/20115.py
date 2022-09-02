# pypy3 127376kb / 160ms

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse = True)

res = drinks[0]
for i in range(1, n):
    res += drinks[i] / 2
print(res)