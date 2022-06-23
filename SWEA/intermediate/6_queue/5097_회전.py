import sys
from collections import deque
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = deque(map(int, input().split()))
    
    for _ in range(M):
        tmp = nums.popleft()
        nums.append(tmp)
        
    print(f'#{test_case} {nums[0]}')