# pypy3 115372kb / 128ms

def fibo(n):
    if n == 0:
        result[n] = 0
    elif n == 1 or n == 2:
        result[n] = 1
    else:
        result[n] = fibo(n - 2) + fibo(n - 1)
    return result[n]
    
n = int(input())
result = [0] * (n + 1)
fibo(n)
print(result[n])