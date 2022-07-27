# pypy3 113248kb 108ms

# 피로도증가, 처리할수있는일, 피로도감소, 번아웃
a, b, c, m = map(int, input().split())
burn = 0
work = 0

for _ in range(24):
    if m < burn + a:
        burn -= c # 쉼
        if burn < 0:
            burn = 0
    else:
        burn += a
        work += b
        
print(work)