import sys

N, C = map(int, sys.stdin.readline().split())

house = [int(sys.stdin.readline()) for _ in range(N)]

house.sort() # 오름차순 정렬

min_gap = 1
max_gap = house[-1] - house[0]
result = 0

while min_gap <= max_gap :
    gap = (min_gap + max_gap) // 2
    value = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= value + gap:
            value = house[i]
            count += 1 # 공유기 설치
    if count >= C: # 공유기 더 많이 설치함. 간격 넓힘
        min_gap = gap + 1
        result = gap
    else:
        max_gap = gap - 1

print(result)