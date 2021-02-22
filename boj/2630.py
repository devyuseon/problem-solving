from sys import stdin

N = int(input())
paper = [list(map(int,stdin.readline().split())) for _ in range(N)]
result = []

def check_paper(x, y, l):
    std = paper[x][y]

    for i in range(x, x + l):
        for j in range(y, y + l):
            if std != paper[i][j]:
                check_paper(x, y, l//2)
                check_paper(x, y + l//2, l//2)
                check_paper(x + l//2, y, l//2)
                check_paper(x + l//2, y + l//2, l//2)
                return
    if std == 0:
        result.append(0)
    else:
        result.append(1)


check_paper(0, 0, N)
print(result.count(0))
print(result.count(1))