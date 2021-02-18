import sys

S = set()

N = int(input())
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "add":
        print(S.add(command[1])
    elif command[0] == "remove":
        print(S.remove(command[1])
    elif command[0] == "check":
        if command[1] in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in S:
            S.remove(command[1])
            S.add(command[1])
        else:
            S.add(command[1])
    elif command[0] == "all":
        print(S.back())
    elif command[0] == "empty":
        print(S.back()) 
