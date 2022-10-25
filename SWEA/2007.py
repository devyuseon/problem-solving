T = int(input())

for test_case in range(1, T + 1):
    txt = input()
    res = ''
    for s in txt:
        res += s
        length = len(res)
        if res == txt[length:length + length]:
            rest = txt[length:]
            rest = rest.replace(res, '')
            if len(rest) < len(res): # 끝에 남음
                break
    print(f'#{test_case} {len(res)}')