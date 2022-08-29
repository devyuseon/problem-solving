# pypy3 115640kb / 152ms

from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0
    
    while q:
        _max = max(q) # 가장 큰 숫자를 뽑아야 함
        v = q.popleft() # 큐의 가장 맨앞
        m -= 1 # 내 위치가 한칸 앞으로
        
        if _max == v: # 큐의 맨앞이 가장 큼
            cnt += 1 # 인쇄됨
            if m < 0: # m == 0이면 큐의 맨앞이 내숫자
                print(cnt)
                break
        else:
            q.append(v) # 큐의 뒤에 추가
            if m < 0:
                m = len(q) - 1 # 뒤로 이동