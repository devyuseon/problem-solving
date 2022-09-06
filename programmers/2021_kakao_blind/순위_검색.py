'''
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0
'''


class Info:
    def __init__(self, lan, job, year, food, score):
        self._lan = lan
        self._job = job
        self._year = year
        self._food = food
        self._score = int(score)

def solution(info, query):
    answer = []
    infos = []
    
    for i in info:
        i = i.split()
        infos.append(Info(i[0], i[1], i[2], i[3], i[4]))
        
    infos.sort(reverse = True, key = lambda x: x._score)
        
    for q in query:
        q = q.split('and')
        
        lan, job, year, food, score = q[0].strip(), q[1].strip(), q[2].strip(), q[3].split()[0], int(q[3].split()[1])
        
        cnt = 0
        for people in infos:
            # 점수
            # 내림차순 정렬이므로 한명이라도 만족 안하면 그만봄
            if people._score < score: break
            
            # 조건
            if lan != '-':
                if people._lan != lan: continue
            if job != '-':
                if people._job != job: continue
            if year != '-':
                if people._year != year: continue
            if food != '-':
                if people._food != food: continue
            
            cnt += 1
        
        answer.append(cnt)
        
    return answer