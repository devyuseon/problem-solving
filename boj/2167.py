# pypy3 116160kb / 164ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * (m + 1)] + [ [0] + list(map(int, input().split())) for _ in range(n)]
k = int(input())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(matrix[x][y] - matrix[x][j - 1] - matrix[i - 1][y] + matrix[i - 1][j - 1])