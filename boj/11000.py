import sys
import heapq

N = int(input())

courses = []
end_time = []

for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    # 시작하는 시간 기준 최소힙
    heapq.heappush(courses, (S, T))

heapq.heappush(end_time, heapq.heappop(courses)[1])

while courses:
    S, T = heapq.heappop(courses)

    if end_time[0] <= S:
        heapq.heappop(end_time)

    heapq.heappush(end_time, T)

print(len(end_time))