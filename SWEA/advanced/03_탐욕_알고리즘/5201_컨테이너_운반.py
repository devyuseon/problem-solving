# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(); t.sort();
    cur = n - 1 # 현재 w 인덱스
    result = []
    
    # 선택한 w의 합이 최대가 되어야 함.
    while t:
        truck = t.pop() # 현재 가장 큰 무게 실을 수 있는 트럭
        if cur > -1:
            while cur > -1:            
                if w[cur] <= truck: # 실을 수 있는 화물 찾음
                    result.append(w[cur])
                    cur -= 1
                    break
                else:
                    cur -= 1
    
    print(f'#{test_case} {sum(result)}')