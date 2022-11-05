# 114328kb / 108ms

squares = [list(map(int, input().split())) for _ in range(4)]
matrix = [[0] * 101 for _ in range(101)]

for square in squares:
    x1, y1, x2, y2 = square
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

cnt = 0
for m in matrix:
    cnt += m.count(1)

print(cnt)