# pypy3 116804kb / 312ms

import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
matrix = [[0] * n for _ in range(n)]

for idx in range(n ** 2):
    student = students[idx]
    candidate = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0: # 빈자리일 경우에만
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if matrix[nx][ny] in student[1:]: # student[1:] 좋아하는 학생
                            like += 1
                        if matrix[nx][ny] == 0:
                            blank += 1
                candidate.append([like, blank, i, j])
    # 좋아하는 학생수 내림차순, 빈칸수 내림차순, 행-열 오름차순
    candidate.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    matrix[candidate[0][2]][candidate[0][3]] = student[0]
    
result = 0
students.sort()

for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] in students[matrix[i][j] - 1][1:]: # [1:] 좋아하는 학생
                    like += 1
        if like != 0:
            result += 10 ** (like - 1)
            
print(result)

'''
<반례1> - O
3
7 9 3 8 2 
5 7 3 8 6
3 5 2 4 9
9 6 8 3 4
8 5 3 1 6
6 3 8 5 4
2 6 4 8 7
1 8 3 4 5
4 7 9 3 8

정답 : 151
완성 배열 :
3 5 8
9 7 6
1 2 4

<반례2> - O
3
2 6 9 3 4 
9 4 5 1 2
3 9 2 1 4
7 8 1 4 6
5 7 3 9 4
1 7 6 8 3
6 9 3 4 5
4 9 7 5 2
8 1 5 3 6

정답 : 143
완성 배열 :
5 9 6
3 2 7
1 4 8

반례 조건 위반 -> https://www.acmicpc.net/board/view/67748

<반례3> - O
4
1 1 2 3 4
2 1 2 3 4
3 1 2 3 4
4 1 2 3 4
5 1 2 3 4
6 1 2 3 4
7 1 2 3 4
8 1 2 3 4
9 1 2 3 4
10 1 2 3 4
11 1 2 3 4
12 1 2 3 4
13 1 2 3 4
14 1 2 3 4
15 1 2 3 4
16 1 2 3 4
답 : 48

완성 배열:
13 5 9 14
6 1 2 7
10 3 4 11
15 8 12 16

'''