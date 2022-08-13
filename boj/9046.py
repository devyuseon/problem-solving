# pypy3 115124kb / 164ms

from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().replace(' ', '').strip() # 공백 삭제
    cnt = Counter(s).most_common()
    flag = True
    if len(cnt) > 1:
        if cnt[0][1] == cnt[1][1]:
            flag = False
    if flag:
        print(cnt[0][0])
    else:
        print('?')