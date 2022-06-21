import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
brackets = {')' : '(', '}' : '{'}

for test_case in range(1, T + 1):
    line = ' '.join(input()).split()
    stack = []
    ans = 1
    
    for s in line:
        if s in brackets.values():
            stack.append(s)
        elif s in brackets.keys():
            # 처음부터 닫는 괄호가 오거나
            # 일치하지 않을 경우
            if len(stack) == 0 or stack[-1] != brackets[s]:
                ans = 0
                break
            if stack[-1] == brackets[s]: # 일치함
                stack.pop()
    
    if len(stack) != 0:
        ans = 0
    
    print(f'#{test_case} {ans}')