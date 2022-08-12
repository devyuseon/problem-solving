def solution(x, y, n):
    flag = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if flag != matrix[i][j]:
                flag = -1
                break
    if flag == -1:
        print('(', end='')
        n //= 2
        solution(x, y, n) # 왼쪽 위
        solution(x, y + n, n) # 오른쪽 위
        solution(x + n, y, n) # 왼쪽 아래
        solution(x + n, y + n, n) # 오른쪽 아래
        print(')', end='')
    
    elif flag == 1:
        print(1, end='')
    else:
        print(0, end='') 

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
solution(0, 0, n)