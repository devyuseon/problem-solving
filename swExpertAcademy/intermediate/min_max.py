import sys
sys.stdin = open("swExpertAcademy\input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    _min = 1000000
    _max = 1
    for n in nums:
        if n < _min: _min = n
        if n > _max: _max = n
    print(f'#{test_case} {_max - _min}')