import sys
input = sys.stdin.readline

def solution(n, m, values):
        

n, k = map(int, input().split())
values = [int(input().strip()) for _ in range(n)]
values = list(set(values))
values.sort(reverse=True)

print(values)