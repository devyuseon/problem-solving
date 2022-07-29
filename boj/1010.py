# pypy3 114328kb / 120ms

from sys import stdin
input = stdin.readline

def factorial(n):
    if n == 0: return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # nCr 계산
    print(factorial(m) // (factorial(n) * factorial(m - n)))