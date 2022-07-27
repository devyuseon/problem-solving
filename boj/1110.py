# pypy3 113112kb / 112ms

origin = int(input())
cnt = 0
n = origin
while True:
    s = str(n) # 문자열화
    if n < 10:
        s = "0" + s
    tmp = str(int(s[0]) + int(s[1]))
    if int(tmp) < 10:
        tmp = "0" + tmp
    n = int(s[1] + tmp[1])
    cnt += 1
    if n == origin:
        break
        
print(cnt)