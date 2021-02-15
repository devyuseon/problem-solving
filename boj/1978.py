import sys

def is_prime(n) -> bool:
    if n == 1:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True

N = int(input())
nums = map(int, sys.stdin.readline().split())

count = 0
for n in nums:
    if is_prime(n) == True:
        count += 1

print(count)

