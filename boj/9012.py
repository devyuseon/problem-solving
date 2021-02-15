import sys

N = int(input())
for _ in range(N):
    brackets = sys.stdin.readline().rstrip()

    stack = []
    is_valid = True
    for cur in brackets:
        if cur == '(':
            stack.append(cur)
            continue
        if not stack:
            is_valid = False
            break
        if cur == ')':
            stack.pop()
            continue

    if not stack and is_valid == True:
        print("YES")
    if stack or is_valid == False:
        print("NO")
