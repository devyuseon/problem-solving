def solution(record):
    from collections import defaultdict
    
    answer = []
    tmp = []
    
    nickname = defaultdict()
    
    for r in record:
        cmd, uid, name = '', '', ''
        splited = r.split()
        if len(splited) == 3:
            cmd, uid, name = splited
        else:
            cmd, uid = splited
        
        if cmd == 'Enter' or cmd == 'Change':
            nickname[uid] = name
        
        if cmd == 'Enter' or cmd == 'Leave':
            tmp.append((uid, cmd))
    
    for s in tmp:
        uid, cmd = s
        
        if cmd == 'Enter':
            answer.append(f'{nickname[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{nickname[uid]}님이 나갔습니다.')
    
    return answer