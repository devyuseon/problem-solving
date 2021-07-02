from collections import deque
import collections
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
    case = collections.deque(sys.stdin.readline().strip().lower())
    if is_palindrome(case):
        print("Yes")
    else:
        print("No")