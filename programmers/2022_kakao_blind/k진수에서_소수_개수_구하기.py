def solution(n, k):
    answer = 0
    
    def is_prime(n):
        for i in range(2, n + 1):
            if i ** 2 > n:
                return True
            if n % i == 0:
                return False
    
    # k진수 구하기
    m = ""
    while n:
        m = str(n % k) + m
        n //= k
        
    # m 자체가 소수일 경우
    if is_prime(int(m)) and '0' not in m:
        return 1
    if m[0] == '0' and is_prime(int(m[1:])) and '0' not in m[1:]: return 1
    if m[len(m) - 1] == '0' and is_prime(int(m[:len(m) - 1])) and '0' not in m[:len(m) - 1]: return 1

    # 앞
    for i in range(0, len(m) - 1):
        if m[i] == '0':
            if is_prime(int(m[:i])):
                answer += 1
            m = m[i:]
            break
    
    # 뒤
    for i in range(len(m) - 1, -1, -1):
        if m[i] == '0':
            if is_prime(int(m[i:])):
                answer += 1
            m = m[:i + 1]
            break

    for num in m.split('0'):
        if num:
            if is_prime(int(num)):
                idx = m.index(num)
                if m[idx - 1] == '0' and m[idx + len(num)] == '0':
                    answer += 1
   
    return answer