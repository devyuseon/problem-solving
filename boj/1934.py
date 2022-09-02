# pypy3 114976kb / 224ms

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd (n, m)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(lcm(n, m))