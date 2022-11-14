S = input()
T = input()
res = 0


def one(m):
    if m[-1] == 'A':
        return True


def two(m):
    if m[0] == 'B':
        return True

def solution(t):
    global res

    if t == S:
        res = 1
        return
    if len(t) < len(S):
        return

    if one(t):
        solution(t[:-1])
    if two(t):
        solution(t[1:][::-1])


solution(T)
print(res)