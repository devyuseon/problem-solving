import sys

while True:
    case = sys.stdin.readline().strip()

    if case == "0":
        break
    
    case = list(case)

    if case == list(reversed(case)):
        print("yes")
    else:
        print("no")