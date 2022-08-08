# pypy3 115056kb / 560ms

n = int(input())
result = 0
for i in range(1, n + 1):
    nums = list(map(int, ' '.join(str(i)).split()))
    cons = i
    for j in nums:
        cons += j
    if cons == n:
        result = i
        break
print(result)