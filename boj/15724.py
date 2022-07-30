# pypy3 141348kb / 756ms

from sys import stdin
input = stdin.readline

'''
                0  0  0  0  0
9 14 29 7   ->  0  9 14  29  7  
1 31 6 13   ->  0 10 45  35 20
21 26 40 16 ->  0 31 71  75 36
8 38 11 23  ->  0 39 109 86 59

1 1 3 2 -> sum([31, 71]) - sum([0, 0])
2 2 3 2 -> sum([31, 71]) - sum([9, 14])
'''

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_sum = [[0] * (m + 1) for _ in range(n + 1)]
t = int(input())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        matrix_sum[i][j] = matrix_sum[i - 1][j] + matrix[i - 1][j - 1]
print(matrix_sum)
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum(matrix_sum[x2][y1 : y2 + 1]) - sum(matrix_sum[x1 - 1][y1 : y2 + 1]))