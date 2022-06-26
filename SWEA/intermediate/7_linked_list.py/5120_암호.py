import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    n = M
    
    for _ in range(K):
        n %= N
        if not n:
            nums.append(nums[-1] + nums[0])
            n -= 1
        else:
            nums.insert(n, nums[n - 1] + nums[n])
        N += 1
        n += M
                        
    print(f'#{test_case}', end=' ')
    print(*nums[-10:][::-1])
    