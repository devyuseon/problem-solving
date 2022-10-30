T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    matrix1 = [m[::-1] for m in list(zip(*matrix))]
    matrix2 = [m[::-1] for m in list(zip(*matrix1))]
    matrix3 = [m[::-1] for m in list(zip(*matrix2))]

    print(f'#{test_case}')
    for i in range(n):
        print(''.join(map(str, matrix1[i])), ''.join(map(str, matrix2[i])), ''.join(map(str, matrix3[i])))
