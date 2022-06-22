import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())

def divide(start, end):
    if start == end: # 그룹 1명됨
        return start 
    
    x = divide(start, (start + end) // 2)
    y = divide((start + end) // 2 + 1, end)
    return fight(x, y)

def fight(x, y):
    global cards
    
    if cards[x] == cards[y]: # 비김
        return x # 작은번호 승
    elif cards[x] - cards[y] == 1 or cards[x] - cards[y] == -2: # x가 이김
        return x
    return y # y가 이김
    
for test_case in range(1, T + 1):
    N = int(input()) # 학생 수
    cards = list(map(int, input().split()))

    print(f'#{test_case} {divide(0, N - 1) + 1}')