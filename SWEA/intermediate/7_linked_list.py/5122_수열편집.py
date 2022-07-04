import sys
sys.stdin = open("SWEA\input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    flag = 1
    
    for _ in range(M):
        cmd = input().split()
        
        if cmd[0] == 'I':
            nums.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == 'D':
            if not nums:
                flag=0
                break
            nums.pop(int(cmd[1]))
        else:
            nums[int(cmd[1])] = int(cmd[2])
            
    if len(nums) > L:
        if flag:
            print(f'#{test_case} {nums[L]}')
        else:
            print(f'#{test_case} -1')
    else:
        print(f'#{test_case} -1')