from collections import deque

a, b = map(int, input().split())
MIN = -1

Q = deque([(a, 1)])
while Q:
    n, count = Q.popleft()
    if n == b:
        MIN = count
        break
    if n * 2 <= b:
        Q.append((n * 2, count + 1))
    if int(str(n) + '1') <= b:
        Q.append((int(str(n) + '1'), count + 1))

print(MIN)

# import sys
# sys.setrecursionlimit(10**7)
    
# def dfs(a, b, cur, count):
#     global MIN
#     if cur == b:
#         MIN = min(MIN, count)
#         MIN += 1
#         return
#     elif cur > b:
#         return
#     else:
#         dfs(a, b, cur * 2, count + 1)
#         dfs(a, b, int(str(cur) + '1'), count + 1)

# a, b = map(int, input().split())
# MIN = sys.maxsize
# dfs(a, b, a, 0)

# print(MIN)