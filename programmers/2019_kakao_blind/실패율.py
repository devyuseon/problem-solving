def solution(N, stages):
    
    people = len(stages)
    fail = {}
    
    for i in range(1, N + 1):
        if people != 0:
            cnt = stages.count(i)
            fail[i] = cnt / people
            people -= cnt
        else:
            fail[i] = 0
    
    return sorted(fail, key = lambda x: fail[x], reverse = True)