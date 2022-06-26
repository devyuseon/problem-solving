import enum
import sys
sys.stdin = open("SWEA\input.txt", "r")

def find_big(nums, n, start, end):
    if start == -1:
        for i, v in enumerate(nums[:end + 1]):
            if v > n:
                return (i, n)
    else:
        for i, v in enumerate(nums[start:]):
            if v > n:
                return (i, n)
    
    return (len(nums), 0) # 큰 숫자 없음
        
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(M)]
    result = nums[0]
    pre = (0, 0) # index, number
    
    for i in range(1, M):
        start, end = -1, -1
        if pre[1] < nums[i][0]:
            start = pre[0]
        else:
            end = pre[0]
            
        idx, num = find_big(result, nums[i][0], start, end)
        if idx < len(result): # 큰 수가 있음
            result = result[:idx] + nums[i] + result[idx:]
            pre = (idx + 1, nums[i][0])
        else:
            result += nums[i]
            pre = (len(result), nums[i][0])
            
    print(f'#{test_case} ', end = '')
    for i in range(1, 11):
        if i >= len(result) - 1:
            break
        else:
            print(result[-i], end = ' ') 
    print()