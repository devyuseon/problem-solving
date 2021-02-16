N, K = map(int, input().split())

li = [i for i in range(1, N + 1)]
result = []
cur = 0

for _ in range(N):
    cur %= N
    next = 0
    
    while True:
        # next가 K가 되면 제거
        if next == K - 1 and li[(cur + next) % N] != -1:
            result.append(li[(cur + next) % N])
            li[(cur + next) % N] = -1
            cur += K
            break
        # 제거 된 인덱스일 경우
        if li[(cur + next) % N] == -1:
            cur += 1
            continue
        # 아무것도 해당하지 않을경우 next증가
        next += 1
            
print("<", end="")
for i, n in enumerate(result):
    if i == len(result) - 1:
        print(n, end="")
    else:
        print(n, end=", ")
print(">")