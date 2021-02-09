import sys

while True:
    case = sys.stdin.readline().strip()

    if case == "0":
        break

    if case == case[::-1]:
        print("yes")
    else:
        print("no")