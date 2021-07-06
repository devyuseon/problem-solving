import sys
from typing import List

def is_palindrome(case: List):
    front = 0
    back = len(case) - 1

    while(front < back):
        if case[front] is not case[back]:
            return False
        front += 1
        back -= 1
    return True

def find_palindrome(words: List):
    if len(words) < 2:
        return '0'

    front = 0
    back = 1
    while(front < back and front < len(words) - 1):
        tmp_1 = words[front] + words[back]
        tmp_2 = words[back] + words[front]

        if is_palindrome(tmp_1):
            return tmp_1
        elif is_palindrome(tmp_2):
            return tmp_2
        else:
            back += 1

        if back == len(words):
            front += 1
            back = front + 1
    return '0'

T = int(input())
for _ in range(T):
    words = []
    k = int(input())
    for _ in range(k):
        words.append(sys.stdin.readline().strip())
    print(find_palindrome(words))