import sys

input = sys.stdin.readline

n = int(input())
# 0-5 / 1-3 / 2-4
dice = [list(map(int, input().split())) for _ in range(n)]
res = 0
pair = {0: 5, 1: 3, 2: 4, 5: 0, 3: 1, 4: 2}


def find_max(d, top, bottom):
    tmp = []

    for num in d:
        if num == top or num == bottom:
            continue
        else:
            tmp.append(num)

    return max(tmp)


def solution(top, init):
    global res

    _sum = init
    for d in dice[1:]:
        bottom = top
        top = d[pair[d.index(top)]]
        _sum += find_max(d, top, bottom)

    res = max(res, _sum)


for i in range(6):
    a, b = dice[0][i], dice[0][pair[i]]  # 윗면, 아랫면 숫자
    init = find_max(dice[0], a, b)
    solution(a, init)
    solution(b, init)

print(res)