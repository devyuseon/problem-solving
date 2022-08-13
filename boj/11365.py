# pypy3 113248kb / 116ms

import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if line.rstrip() == 'END' : break
    print(line[::-1])