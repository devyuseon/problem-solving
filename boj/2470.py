# pypy3 128500kb / 156ms

def solution():  
    left, right = 0, len(val) - 1
    now = (10**9 * 2 + 1, 0, right)
    
    while left < right:
        tmp = val[left] + val[right]
        if now[0] > abs(tmp):
            now = (abs(tmp), val[left], val[right])
        if tmp > 0:
            right -= 1
        elif tmp == 0:
            return val[left], val[right]
        else:
            left += 1
    return now[1], now[2]
    
n = int(input())
val = list(map(int, input().split()))
val.sort()
print(*solution())