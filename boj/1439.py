def solution(string: str):
    status = string[0]
    zero_cnt = 0
    one_cnt = 0

    for i in range(1, len(string)):
        if status == string[i]:
            continue
        else:
            if status == '0':
                zero_cnt += 1
            if status == '1':
                one_cnt += 1
            status = string[i]
    
    if status == '0': zero_cnt += 1
    if status == '1': one_cnt += 1
    
    return(min(zero_cnt, one_cnt))

"""
def solution(string: str):
    zero_frac = string.split('1')
    one_frac = string.split('0')
    zero_cnt = 0
    one_cnt = 0

    for s in zero_frac:
        if s != '':
            zero_cnt += 1
    for s in one_frac:
        if s != '':
            one_cnt += 1

    return(min(zero_cnt, one_cnt))
"""

string = input()
print(solution(string))