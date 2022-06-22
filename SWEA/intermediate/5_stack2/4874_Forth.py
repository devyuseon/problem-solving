import sys
from collections import deque
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())

def calculate(x, y, op):
    x = int(x)
    y = int(y)
    if op == '/' : return x // y
    elif op == '*' : return x * y
    elif op == '+' : return x + y
    elif op == '-' : return x - y

for test_case in range(1, T + 1):
    code = deque(input().split())
    stack = []
    result = 'error'
   
    print(f'#{test_case} ', end = '')
    for _ in range(len(code) - 1):
        s = code.popleft()
        try:
            if s.isdigit(): # 숫자이면 스택에 넣음
                stack.append(s)
            elif s in ('/', '+', '-', '*'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calculate(num1, num2, s))
        except:
            break
    
    if code.pop() == '.':
        if len(stack) == 1:
            result = stack.pop()
            
    print(result)