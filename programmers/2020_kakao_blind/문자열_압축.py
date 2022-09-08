'''
채점 결과
정확성: 96.0
합계: 96.0 / 100.0
'''

def solution(s):
    answer = 1000
    n = len(s)
    
    prev = ''
    cnt = 1
    compressed = ''
    for i in range(1, n):
        for j in range(0, n, i):
            if prev == s[j : j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += prev
                else:
                    compressed += (str(cnt) + prev)
                prev = s[j : j + i]
                cnt = 1
                
        if cnt != 1:
            compressed += (str(cnt) + prev)
        else:
            compressed += prev
            
        answer = min(answer, len(compressed))
        prev = ''
        cnt = 1
        compressed = ''
        
    return answer