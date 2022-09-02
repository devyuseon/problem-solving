# pypy3 115004kb / 124ms
# https://myjamong.tistory.com/139

def is_prime(x):
    flag = True
    for i in range(2, x + 1):
        if i * i > x: break
        if x % i == 0:
            flag = False
            break
    return flag

m = int(input())
n = int(input())

res = 0
_min = 0
for i in range(m, n + 1):
    if i != 1 and 1 != 2:
        if is_prime(i):
            res += i
            if _min == 0:
                _min = i

if res != 0: print(res)
if _min == 0: print(-1)
else: print(_min)