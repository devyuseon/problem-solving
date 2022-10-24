T = int(input())
table = {s: i for i, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

for test_case in range(1, T + 1):
    txt = list(input())
    res, bins = '', ''

    for s in txt:
        bins += str(bin(table[s])[2:]).zfill(6)  # 0b 제거

    for i in range(0, len(bins), 8):
        v = int(bins[i: i + 8], 2)
        res += chr(v)

    print(f'#{test_case} {res}')
