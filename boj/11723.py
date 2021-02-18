import sys

S = set()
nums = [i for i in range(1,21)]

N = int(input())
for _ in range(N):
    command = sys.stdin.readline().split()

    if len(command) == 1:
        if command[0] == "all":
            S.update(nums)
        if command[0] == "empty":
            S = set()
        continue
    
    n = int(command[1])
    if command[0] == "add":
        S.add(n)
    if command[0] == "remove":
        S.discard(n)
    if command[0] == "check":
        if n in S:
            print(1)
        else:
            print(0)
    if command[0] == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)