# https://msiqoc.tistory.com/28

from itertools import combinations

def solution(relation):
    answer = 0
    rows = len(relation)
    cols = len(relation[0])
    
    #유일성
    candidates = []
    for i in range(1, cols+1):
        candidates.extend(combinations(range(cols), i)) 
        
    final = []
    for c in candidates:
        tmp = [tuple(item[key] for key in c) for item in relation] 
        if len(set(tmp)) == rows:
            final.append(c)
    
    answer = set(final) 
    
    # 최소성
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
 
    return len(answer)