from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    idx = int(input())
    nums = list(map(int, input().split()))

    print(f'#{test_case} {Counter(nums).most_common()[0][0]}')