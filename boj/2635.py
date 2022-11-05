n = int(input())
res = []
ans = [0, []]

def solution(m):
    li = [n, m]
    while True:
        tmp = li[-2] - li[-1]
        if tmp < 0:
            break
        else:
            li.append(tmp)
    res.append(li)


for i in range(n + 1):
    solution(i)


for li in res:
    if ans[0] < len(li):
        ans = [len(li), li]

print(ans[0])
print(*ans[1])