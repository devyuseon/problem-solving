import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # N: 수열의 길이, M: 추가 횟수, L: 출력할 인덱스
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    add = [tuple(map(int, input().split())) for _ in range(M)] # (인덱스, 숫자)
    
    for idx, num in add:
        nums.insert(idx, num)
                        
    print(f'#{test_case} {nums[L]}')