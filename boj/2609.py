import collections

def get_prime_factor(n) -> dict:
    dic = collections.defaultdict(int)
    i = 2

    while i <= n:
        if n % i == 0:
            dic[i] += 1
            n = n/i
        else:
            i += 1
    
    return dic

N, M = map(int, input().split())

# 소인수분해
N_prime_factor = get_prime_factor(N) 
M_prime_factor = get_prime_factor(M)

# 소인수 가짓수 많은것을 M으로 설정
if len(N_prime_factor) > len(M_prime_factor):
    N_prime_factor, M_prime_factor = M_prime_factor, N_prime_factor

great, least = 1, 1 # 곱할꺼니까 1로 초깃값 설정

# 최대공약수 구하기
great_dic = collections.defaultdict(int)
for k in N_prime_factor.keys():
    great_dic[k] = min(N_prime_factor[k], M_prime_factor[k])

for k, v in great_dic.items():
    great *= pow(k,v)

# 최소공배수 구하기
least_dic = collections.defaultdict(int)
for k in M_prime_factor.keys():
    if k not in N_prime_factor:
        least_dic[k] = M_prime_factor[k]
    else:
        least_dic[k] = max(N_prime_factor[k], M_prime_factor[k])

for k, v in least_dic.items():
    least *= pow(k,v)

print(great)
print(least)