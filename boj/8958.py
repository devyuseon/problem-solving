def get_score(case, score):
    conti = 0
    for s in case:
        if s == 'O':
            conti += 1
        if s == 'X':
            conti = 0
        score += conti
    return score

n = int(input())
for _ in range(0,n):
    case = input()
    print(get_score(case,0))