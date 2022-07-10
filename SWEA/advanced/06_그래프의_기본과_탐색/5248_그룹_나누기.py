# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

import sys
sys.stdin = open("SWEA\input.txt", "r")

def find(x):    
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    a = find(x)
    b = find(y)
    
    if a > b: parent[a] = b
    else: parent[b] = a
    

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    # 부모는 자기 자신
    parent = [i for i in range(n + 1)]
    group = set()
    
    for i in range(0, m * 2, 2):
        union(nums[i], nums[i + 1])
        
    for i in parent:
        group.add(find(i))
        
    print(f'#{test_case} {len(group) - 1}')