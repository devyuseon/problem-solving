result = [[1, 0], [0, 1]]

N = int(input())
Q = [int(input()) for _ in range(N)]

if max(Q) > 1:
    for i in range(2, max(Q) + 1):
        tmp = [result[i-2][0] + result[i-1][0], result[i-2][1] + result[i-1][1]]
        result.append(tmp)

for n in Q:
    print(result[n][0], result[n][1])