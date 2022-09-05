def solution(fees, records):
    # fees: 기본시간, 기본요금, 단위시간, 단위요금
    
    from collections import defaultdict
    import math
    
    def calc_time(in_time, out_time):
        
        in_h, in_m = map(int, in_time.split(':'))
        out_h, out_m = map(int, out_time.split(':'))
            
        calc = 0
            
        if out_m >= in_m:
            calc += out_m - in_m
            calc += (out_h - in_h) * 60
        else:
            calc += 60 - in_m + out_m
            calc += (out_h - in_h - 1) * 60
        
        return calc

    def calc_fee(time):
        fee = fees[1] # 기본 요금
        if time > fees[0]: # 기본 시간 초과
            if (time - fees[0]) % fees[2] == 0:
                fee += (time - fees[0]) // fees[2] * fees[3]
            else:
                fee += ((time - fees[0]) // fees[2] + 1) * fees[3]
        return fee
        
    
    dict = defaultdict(list)
    times = defaultdict(int)
    result = []
    answer = []
    
    for record in records:
        time, id, info = record.split()
        
        if dict[id]: # 입차한 기록이 있으면
            in_time = dict[id].pop()                
            times[id] += calc_time(in_time, time)
        else: # 입차한 기록이 없으면
            dict[id].append(time)
    
    for k, v in dict.items(): # 입차하고 출차한 기록이 없는 경우
        if v:
            times[k] += calc_time(v.pop(), "23:59")
            
    for k, v in times.items():
        result.append((k, calc_fee(v)))
        
    for time, fee in sorted(result):
        answer.append(fee)
       
    return answer