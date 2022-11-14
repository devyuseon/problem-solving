k = int(input())
max_height, max_height_idx = 0, 0
max_width, max_width_idx = 0, 0
info = []

for i in range(6):
    d, n = map(int, input().split())
    info.append([d, n])
    if d == 1 or d == 2: # 가로 길이라면
        if max_width < n:
            max_width, max_width_idx = n, i
    else:
        if max_height < n:
            max_height, max_height_idx = n, i

# 인접한 변 +1, -1 로 찾을 수 있음. 가로변에 붙은 두 세로변과 가장 긴 가로, 세로 인덱스 저장
idx_li = [info[max_height_idx - 1], info[(max_height_idx + 1) % 6], info[max_width_idx - 1],
              info[(max_width_idx + 1) % 6]]

product = 1 # 곱을 저장할 변수
for i in info:
    if i not in idx_li:
        product *= i[1]

print((max_width * max_height - product) * k)