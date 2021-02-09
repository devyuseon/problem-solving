import sys

T = int(input())
for _ in range(0, T):
    H, W, N = map(int, sys.stdin.readline().split())
    # 방 호수는 "나머지 + 몫+1" 로 구성됨 
    q = N // H
    c = N % H

    # 맨 꼭대기 층일때, 나누어 떨어질때
    if c == 0:
        c = H

    print(str(c) + (str(q + 1)).zfill(2))