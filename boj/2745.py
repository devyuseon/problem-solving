# pypy3 113248kb / 124ms

n, b = input().split()
b = int(b)
ans = 0

for m, val in enumerate(n[::-1]): # m: 거듭제곱
    try:
        num = int(val)
        ans += num * (b ** m)
    except: # 알파벳일때
        ans += (ord(val) - 55) * (b ** m)

print(ans)