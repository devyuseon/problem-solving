from collections import deque
import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 화덕의 크기, 피자 갯수
    pizzas = deque(enumerate(list(map(int, input().split())), 1)) # 피자의 치즈 양. 시작인덱스 1
    oven = deque()
    
    # 오븐 초기화
    for _ in range(N):
        oven.append(pizzas.popleft())

    # 오븐은 계속 회전하고.. 1번자리에 올때마다 //2 되어있음.
    while len(oven) > 1:
        # 오븐 공간 남으면 피자 넣어줌
        if len(oven) < N and pizzas:
            oven.append(pizzas.popleft())
        
        num, cheese = oven.popleft()
        # 치즈 양이 0이라면 화덕에서 뺌
        if not cheese // 2:
            continue
        else:
            oven.append((num, cheese // 2))
                        
    print(f'#{test_case} {oven.popleft()[0]}')