# pypy3 126240kb / 376ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]       

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2] + matrix[x1 - 1][y1 - 1])