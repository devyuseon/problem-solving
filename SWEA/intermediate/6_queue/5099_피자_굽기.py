import sys
sys.stdin = open("SWEA\input.txt", "r")

'''
한 바퀴 돌때마다 n//2로 치즈 양 줄어듦.
0되면 빼고 그자리에 뒤에것들 넣음
이때, 화덕의 번호(임의로 정함) 가 작은것이 먼저빠짐
그러나 피자의 번호는 기억하고 있어야 함.
'''

def find_zero(oven):
    tmp = []
    for i, v in enumerate(oven):
        # v[0] = False이면 꺼내고 채우지 않은 화덕
        #        0이면 아직 채우지 않은 화덕이다.
        # v[1] = 치즈양
        if v[0] != 21 and v[1] == 0:
            tmp.append(i)
    # tmp => 작은번호 순으로 0인 원소 index 들어감
    # 이때 index는 '화덕 번호'
    return tmp

def divide_two(pizza):
    return (pizza[0], pizza[1] // 2)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 화덕의 크기, 피자 갯수
    pizzas = list(map(int, input().split())) # 피자의 치즈 양
    oven = [(0, 0)] * N # 화덕 (피자번호, 치즈양)  
    result = [] # 꺼낸 피자번호 순서 리스트
    cur = 0 # 피자 넣는 index
    
    for i in range(N):
        oven[i] = (cur, pizzas[cur])
        cur += 1

    # 한 바퀴가 while 한 바퀴.
    while len(result) != M:
        
        zeros = find_zero(oven) # 치즈 양이 0인 화덕
        
        for i in zeros:
            # 순서대로 result에 넣어줌 (처음이 아닐 경우)
            result.append(oven[i][0]) # 피자 번호
            oven[i] = (21, 0) # 꺼낸 피자 표시
            
            if cur < M:
                # 남은 피자 화덕에 넣음
                oven[i] = (cur, pizzas[cur])
                cur += 1
        
        # oven 한바퀴 돌때 모든 치즈 양들이 //2
        oven = list(map(divide_two, oven))
                        
    print(f'#{test_case} {result[-1] + 1}')