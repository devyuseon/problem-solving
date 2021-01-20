import sys


def sub_sum(N: int, S: int, list: list) -> int:
    min_length = sys.maxsize
    start = 0
    now_sum = 0
    for index, int in enumerate(list):
        if sum(list[start:index]) >= S:
            min_length = min(min_length, index - start)
            start += 1
            index -= 1
        else:
            continue
    return min_length


N, S = 10, 15
list = list(map(int, "5 1 3 5 10 7 4 9 2 8".split()))

# print(sub_sum(N, S, list))
print(sub_sum(N, S, list))
