import sys

N = int(input())

list = [int(sys.stdin.readline().strip()) for _ in range(N)]

for n in sorted(list) : print(n)