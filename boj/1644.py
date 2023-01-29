n = int(input())
dp = [False, False] + [True] * (n - 1)
primes = [0]

for i in range(1, n + 1):
    if dp[i]:
        primes.append(i)
        j = 2
        while i * j <= n:
            dp[i * j] = False
            j += 1

for i in range(1, len(primes)):
    primes[i] = primes[i - 1] + primes[i]

left, right = 0, 1
cnt = 0

while right < len(primes):
    _sum = primes[right] - primes[left]
    if _sum == n:
        cnt += 1
        left += 1
        right += 1
    elif _sum < n:
        right += 1
    elif _sum > n:
        left += 1

print(cnt)