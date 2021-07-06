# 투포인터 풀이

import sys

def is_palindrome(case: list):
    front = 0
    back = len(case) - 1

    while(front < back):
        if case[front] is not case[back]:
            return False
        front += 1
        back -= 1
    return True


N = int(input())
for _ in range(N):
    case = sys.stdin.readline().strip().lower()
    if is_palindrome(case):
        print("Yes")
    else:
        print("No")

"""
# Pop
from collections import deque
from typing import Deque
import sys

def is_palindrome(case: Deque):
    while(len(case) > 1):
        if case.popleft() is not case.pop():
            return False
        else:
            continue
    return True

N = int(input())
for _ in range(N):
    case = deque(sys.stdin.readline().strip().lower())
    if is_palindrome(case):
        print("Yes")
    else:
        print("No")
"""