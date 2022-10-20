T = int(input())

for test_case in range(1, T + 1):

    tmp = input().split()
    nums = list(tmp[0])
    change = int(tmp[1])
    res = 0

    def cal(li):
        return int(''.join(s for s in li))

    def dfs(li, cnt):
        global res

        if cnt == change:
            res = max(res, cal(li))
            return

        for i in range(len(li)):
            for j in range(i + 1, len(li)):
                li[i], li[j] = li[j], li[i]
                tmp = ''.join(li)
                if visited.get((tmp, cnt), 1):
                    visited[(tmp, cnt)] = 0
                    dfs(li, cnt + 1)
                li[i], li[j] = li[j], li[i]

    visited = {}
    dfs(nums, 0)
    print(f'#{test_case} {res}')