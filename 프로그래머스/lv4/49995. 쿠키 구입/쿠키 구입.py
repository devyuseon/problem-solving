from itertools import accumulate

def solution(cookie):

    res, n = 0, len(cookie)

    for m in range(len(cookie)):
        a = set(accumulate(reversed(cookie[:m + 1])))
        b = set(accumulate(cookie[m + 1:]))
        c = a & b
        
        if c:
            res = max(*c, res)
    
    return res