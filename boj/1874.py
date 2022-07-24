import sys
input = sys.stdin.readline

n = int(input())
stack = []
cur = 1
result = ''
flag = True

for _ in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        cur += 1
        result += '+\n'
    if stack[-1] == num:
        stack.pop()
        result += '-\n'
    else:
        flag = False
        break

if flag:
    print(result.rstrip())
else:
    print('NO')