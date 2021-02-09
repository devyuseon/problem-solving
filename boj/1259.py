import sys
import collections

while True:
    case = sys.stdin.readline().strip()

    if case == "0":
        break
    
    deq = collections.deque(list(map(int,case)))

    while True:
        if len(deq) == 1:
            print("yes")
            break

        left = deq.popleft()
        right = deq.pop()

        if left != right:
            print("no")
            break

        if left == right and len(deq) == 0:
            print("yes")
            break