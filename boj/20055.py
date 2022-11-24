import sys
from collections import deque

n, k = map(int, input().split())
nums = deque(list(map(int, input().split())))
robots = deque([0 for i in range(2 * n)])

cnt = 1

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    nums.rotate(1)
    robots.rotate(1)

    # 내리는 위치(n번칸) 확인
    if robots[n - 1] > 0:
        robots[n - 1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    if sum(robots) != 0:
        _min = sys.maxsize
        _min_idx = 2 * n
        for i, v in enumerate(robots):
            if v != 0 and v < _min:
                _min, _min_idx = v, i

        for i in range(2 * n - 1):
            idx = _min_idx - i
            if idx < 0:
                idx = 2 * n + idx

            if robots[idx] != 0:
                nidx = (idx + 1) % (2 * n)
                if robots[nidx] == 0 and nums[nidx] > 0:
                    robots[nidx] = robots[idx]
                    robots[idx] = 0
                    nums[nidx] -= 1

        # 내리는 위치(n번칸) 확인
        if robots[n - 1] > 0:
            robots[n - 1] = 0

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if nums[0] > 0 and robots[0] == 0:
        nums[0] -= 1
        robots[0] = cnt

    if nums.count(0) >= k:
        break
    else:
        cnt += 1

print(cnt)
