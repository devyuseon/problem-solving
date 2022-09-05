def solution(id_list, report, k):
    from collections import defaultdict
    
    count = defaultdict(set)
    result = defaultdict(int)
    answer = []
    
    for r in report:
        user, target = r.split()
        count[target].add(user)
    
    for key, val in count.items():
        if len(val) >= k: # key 유저는 정지됨
            for user in val:
                result[user] += 1
    
    for id in id_list:
        if id in result.keys():
            answer.append(result[id])
        else:
            answer.append(0)
            
    return answer