T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    _max = price[n - 1]
    res = 0

    for i in range(n - 2, - 1, -1):
        if price[i] >= _max:
            _max = price[i]
        else:
            res += _max - price[i]

    print(f'#{test_case} {res}')
