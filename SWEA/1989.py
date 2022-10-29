from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    txt = deque(list(input().rstrip()))
    res = 1

    while len(txt) > 1:
        if txt.popleft() != txt.pop():
            res = 0
            break

    print(f'#{test_case} {res}')