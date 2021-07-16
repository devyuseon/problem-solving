import sys

def solution(L: int, P: int, V: int):
    result = 0

    while True:
        if V - P > 0:
            result += L
            V -= P
        else:
            if V > L:
                result += L
            else:
                result += V
            return result

def solution2(L: int, P: int, V: int):
    result = 0
    result += (V // P) * L

    carry = V % P
    V -= (V // P) * P
    
    if carry > L:
        return result + L
    else:
        return result + V

i = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if V == 0: break
    print(f"Case {i}: {solution(L, P, V)}")
    i += 1