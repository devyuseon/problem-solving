import sys

locations = []

N = int(input())
for _ in range(N):
    (x, y) = map(int, sys.stdin.readline().split())
    locations.append((x,y))

result = sorted(locations, key= lambda x: (x[0],x[1]))

for li in result:
    print(li[0], li[1])