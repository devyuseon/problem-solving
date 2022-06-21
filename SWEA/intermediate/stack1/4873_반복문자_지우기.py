import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    case = input()
    stack = []
    
    for s in case:
        if not stack or s != stack[-1]:
            stack.append(s)
        elif stack or s == stack[-1]:
            stack.pop()
            
    print(f'#{test_case} {len(stack)}')
        