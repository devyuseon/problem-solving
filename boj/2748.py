# pypy3 113248kb / 108ms

n = int(input())
fibo = [0] * (n + 3)
fibo[0] = 1; fibo[1] = fibo[2] = 1

if n > 2:
    idx = 3
    while idx <= n:
        fibo[idx] = fibo[idx - 2] + fibo[idx - 1]
        idx += 1

print(fibo[n])