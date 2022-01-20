import sys
    
N, K = map(int, input().split())
product = list(map(int, input().split()))
multitab = [0] * N
result = 0

for i in range(K):
    # 꽂혀있으면 안뽑아도됨
    if product[i] in multitab:
        continue
    # 멀티탭에 비어있는 자리있으면 꽂음
    elif 0 in multitab:
        multitab[multitab.index(0)] = product[i]
    # 꽉차있는데 꽂혀있지도 않음. 뽑아야함
    else:
        idx = -sys.maxsize
        isExist = True # 등장함/안함 판별
        for k, v in enumerate(multitab):
            if v not in product[i + 1:]:
                # 앞으로 등장 안하는 가전제품은
                multitab[k] = product[i] # 뽑아버림
                isExist = False
                break
            else:
                # 최대한 나중에 등장하는것 찾기
                # idx는 order의 인덱스
                idx = max(idx, product[i + 1:].index(v) + i + 1)
        if idx != -sys.maxsize and isExist == True:
            multitab[multitab.index(product[idx])] = product[i] # 뽑기   
        result += 1 # 뽑았으니 1증가

print(result)