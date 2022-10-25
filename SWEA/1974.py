import pprint

T = int(input())

for test_case in range(1, T + 1):
    def square():
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = [0 for i in range(10)]
                for k in range(3):
                    for l in range(3):
                        if check[matrix[i + k][j + l]] == 0:
                            check[matrix[i + k][j + l]] = 1
                        else:
                            return False
        return True

    def line():
        for i in range(9):
            check_r = [0 for _ in range(10)]
            check_c = [0 for _ in range(10)]
            for j in range(9):
                if check_r[matrix[i][j]] == 0:
                    check_r[matrix[i][j]] = 1
                else:
                    return False
                if check_c[matrix[j][i]] == 0:
                    check_c[matrix[j][i]] = 1
                else:
                    return False
        return True


    matrix = [list(map(int, input().split())) for _ in range(9)]
    print('#' + str(test_case), end=' ')
    if square() and line():
        print('1')
    else:
        print('0')