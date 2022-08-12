# pypy3 129236kb / 128ms

def solution(x):
    if x == 1:
        return ['*']
    
    stars = solution(x // 3)
    pat = []
    
    for s in stars:
        pat.append(s * 3)
    for s in stars:
        pat.append(s + ' ' * (x // 3) + s)
    for s in stars:
        pat.append(s * 3)
    return pat

n = int(input())
print('\n'.join(solution(n)))