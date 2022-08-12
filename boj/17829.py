# pypy3 127804kb / 368ms

import sys
input = sys.stdin.readline

def pooling(matrix): 
    if len(matrix) == 1:
        print(*matrix[0])
        return
        
    new = []    
    for i in range(0, len(matrix), 2):
        tmp = []
        for j in range(0, len(matrix), 2):
            tmp.append(sorted([matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]])[-2])
        new.append(tmp)
    pooling(new)
        

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
pooling(nums)