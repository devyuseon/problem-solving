N = int(input())

count = 0

while N != 1:
    # 2, 3일경우
    if N == 2 or N == 3:
        count += 1
        break
    
    # 3으로 나누어 떨어짐
    if N % 3 == 0:
        N /= 3
        count += 1
        continue

    # 3으로 나눴을때 나머지 1
    if N % 3 == 1:
        N -= 1
        count += 1
        continue
    
    # 2로 나누어 떨어짐
    if N % 2 == 0:
        N /= 2
        count += 1
        continue

    # 2로 나눴을때 나머지 1
    if N % 2 == 1:
        N -= 1
        count += 1
        continue

print(count)