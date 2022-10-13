from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dz = [(-1, -1), (1, -1), (1, 1), (-1, 1)] # 대각선왼쪽위, 오른쪽위, 오른쪽아래, 왼쪽아래

n, m, k, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
herb = [[0] * n for _ in range(n)]
ans = 0 # 박멸한 나무의 수


def grow(): # 나무의 성장
    for i in range(n):
        for j in range(n):
            # 나무가 있을 경우
            if matrix[i][j] > 0:
                cnt = 0 # 성장할 정도 계산
                # 상하좌우를 살펴봄
                for p in range(4):
                    x, y = i + dx[p], j + dy[p]
                    # 좌표가 범위 안이고
                    if 0 <= x < n and 0 <= y < n:
                        if matrix[x][y] > 0: # 나무가 있을 경우
                            cnt += 1
                matrix[i][j] += cnt


def spread(): # 나무의 번식
    tmp_matrix = deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            # 나무가 있을 경우
            if tmp_matrix[i][j] > 0 and not herb[i][j]:
                candi = [] # 번식 가능한 칸
                # 상하좌우를 살펴봄
                for p in range(4):
                    x, y = i + dx[p], j + dy[p]
                    # 좌표가 범위 안이고
                    if 0 <= x < n and 0 <= y < n:
                        # 빈칸
                        if tmp_matrix[x][y] == 0 and not herb[x][y]:
                            candi.append((x, y))
                # 번식 진행
                if candi:
                    tmp = tmp_matrix[i][j] // len(candi)
                    for x, y in candi:
                        matrix[x][y] += tmp

def find_most_kill():
    global ans
    _max, _x, _y = 0, 0, 0
    for i in range(n):
        for j in range(n):
            # 나무가 있을 경우
            if matrix[i][j] > 0:
                cnt = matrix[i][j] # 박멸 가능한 나무 계산
                # 대각선 네방향 살펴봄
                for p in range(4):
                    x, y = i, j
                    for _ in range(k):
                        x, y = x + dz[p][0], y + dz[p][1]
                        # 좌표가 범위 안이고
                        if 0 <= x < n and 0 <= y < n:
                            if matrix[x][y] > 0:
                                cnt += matrix[x][y]
                            else: break
                        else: break
                if cnt > _max:
                    _max = cnt
                    _x, _y = i, j
    ans += _max
    return _x, _y

def kill(x, y):
    herb[x][y] = c
    matrix[x][y] = 0
    for p in range(4):
        i, j = x, y
        for _ in range(k):
            i, j = i + dz[p][0], j + dz[p][1]
            # 좌표가 범위 안이고
            if 0 <= i < n and 0 <= j < n:
                if matrix[i][j] != -1:
                    herb[i][j] = c  # 제초제
                    matrix[i][j] = 0
                if matrix[i][j] == 0 or matrix[i][j] == -1:
                    break
            else:
                break

def age():
    for i in range(n):
        for j in range(n):
            if herb[i][j] > 0:
                herb[i][j] -= 1

for _ in range(m):
    grow() # 성장
    spread() # 번식
    age() # 제초제 나이 감소
    x, y = find_most_kill() # 제초제 위치 선정
    kill(x, y) # 제초제 뿌리기

    # 제초제 나이 -1


print(ans)