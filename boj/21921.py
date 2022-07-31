n, x = map(int, input().split())
visitor = list(map(int, input().split()))

# 슬라이딩 윈도우 pypy3 148308kb / 212ms
if max(visitor) == 0:
    print('SAD')
else:
    tmp = sum(visitor[:x])
    _max = tmp
    cnt = 1
    
    for i in range(x, n):
        # 윈도우 i - x + 1 부터 i까지
        tmp -= visitor[i - x] # 윈도우 전값 -
        tmp += visitor[i] # 윈도우 앞값 +
        if tmp > _max:
            _max = tmp
            cnt = 1
        elif tmp == _max:
            cnt += 1
    print(_max)
    print(cnt)

# 투포인터 풀이 pypy3 148308kb / 176ms
# start, end = 0, x - 1
# _max = 0
# tmp = sum(visitor[:x])
# cnt = 0
# while end < n:
#     if _max == tmp:
#         cnt += 1
#     elif _max < tmp:
#         cnt = 1
#         _max = tmp
    
#     if end == n - 1:
#         break    
    
#     tmp -= visitor[start]
#     start += 1
#     end += 1
#     tmp += visitor[end]
    
# if _max == 0:
#     print('SAD')
# else:
#     print(_max)
#     print(cnt)