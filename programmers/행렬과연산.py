from collections import deque

def solution(rc, operations):
    left = deque([r[0] for r in rc])
    mid = deque([deque(r[1:-1]) for r in rc])
    right = deque([r[-1] for r in rc])

    def shiftrow():
        left.appendleft(left.pop())
        mid.appendleft(mid.pop())
        right.appendleft(right.pop())

    def rotate():
        mid[0].appendleft(left.popleft())
        right.appendleft(mid[0].pop())
        mid[-1].append(right.pop())
        left.append(mid[-1].popleft())

    for op in operations:
        if op == "ShiftRow":
            shiftrow()
        else:
            rotate()

    return [[left[i]] + list(mid[i]) + [right[i]] for i in range(len(rc))]