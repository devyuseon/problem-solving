
from itertools import product

def solution(users, emoticons):
    answer = []
    n = len(users)

    sale = [10, 20, 30, 40] # 할인율    
    cases = set()

    cases = product(sale, repeat=len(emoticons))
            
    for case in cases:
        pay = [0 for _ in range(n)]
        member = 0
        for i in range(len(emoticons)):
            for j in range(n):
                if pay[j] == -1:
                    continue
                if users[j][0] > case[i]:
                    continue
                pay[j] += emoticons[i] * (1 - case[i] * 0.01)
                if pay[j] >= users[j][1]:
                    pay[j] = -1 # 이모티콘 플러스 가입
                    member += 1
        tmp = 0
        for p in pay:
            if p != -1:
                tmp += p
        answer.append([member, tmp])

    answer.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    return [answer[0][0], int(answer[0][1])]