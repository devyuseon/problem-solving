# pypy3 113112kb / 132ms

def convert(s: str):
    if s.startswith('0'):
        s = s[1]
    return int(s)

h1, m1, s1 = map(convert, input().split(':'))
h2, m2, s2 = map(convert, input().split(':'))

s = s2 - s1
if s < 0:
    s += 60
    m1 += 1
    
m = m2 - m1
if m < 0:
    m += 60
    h1 += 1

h = h2 - h1
if h < 0:
    h += 24

if h == 0 and m == 0 and s == 0:
    print('24:00:00')
elif h >= 24:
    if m != 0 or s != 0:
        print('24:00:00')
else:
    print('{0:02d}:{1:02d}:{2:02d}'.format(h, m, s))