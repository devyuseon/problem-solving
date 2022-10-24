n = int(input())
res = []
for i in range(1, n + 1):
    tmp = ""
    cnt = 0
    for s in str(i):
        if s in ['3', '6', '9']:
            cnt += 1
        else:
            tmp += s
    if cnt == 0:
        res.append(tmp)
    else:
        res.append('-' * cnt)
print(*res)