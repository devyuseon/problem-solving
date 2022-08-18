# pypy3 30퍼 틀림..???

import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())
money = list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)
    
dic = defaultdict(list)
for i, m in enumerate(parent):
    if i == 0: continue
    dic[m].append(money[i - 1])

res = 0

for key in dic.keys():
    res += sorted(dic[key])[0]

if res <= k: print(res)
else: print('Oh no')