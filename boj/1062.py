import sys

def dfs(idx:int, count: int, learn: list, words: list):
    global result
    
    if count == K - 5:
        tmp = 0
        for word in words:
            isContain = True
            for w in word:
                # 한 번이라도 알파벳이 해당 단어에 없으면
                # 배울 수 없다.
                if not learn[ord(w) - ord('a')]:
                    isContain = False
                    break
            if isContain:
                tmp += 1
        result = max(tmp, result)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, count + 1, learn, words)
            learn[i] = False

N, K = map(int, input().split())

# K가 5보다 작으면 antatica(중복제거->5글자) 도 못배움
if K < 5:
    print(0)
    sys.exit()
# K가 26이면 다 배울수 있음
elif K == 26:
    print(N)
    sys.exit()

words = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
learn = [0] * 26
result = 0

# a, c, i, n, t는 무조건 배워야 함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = True

dfs(0, 0, learn, words)

print(result)