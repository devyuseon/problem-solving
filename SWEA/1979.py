T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    # 연속된 수 계산
    def cal():
        global res

        for i in range(n):
            cnt = 0
            for j in range(n):
                if matrix[i][j] == 0:
                    if cnt == k:
                        res += 1
                    cnt = 0
                if matrix[i][j] == 1:
                    cnt += 1
                if j == n - 1:
                    if cnt == k:
                        res += 1

    # 전치행렬 만들기
    def reverse():
        global matrix

        tmp = list(zip(*matrix))
        matrix = tmp

    cal()
    reverse()
    cal()

    print(f'#{test_case} {res}')