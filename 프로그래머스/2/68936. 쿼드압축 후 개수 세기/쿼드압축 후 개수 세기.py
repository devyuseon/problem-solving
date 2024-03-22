import sys
sys.setrecursionlimit(1000000000)

def solution(arr):
    N = len(arr)
    answer = [0, 0]
    
    x1, x2, y1, y2 = 0, N - 1, 0, N - 1
    def dvide_conqure(a1, a2, b1, b2):
        #print(a1, a2, b1, b2)        
        size = (a2 - a1 + 1) * (a2 - a1 + 1)
        tmp = 0
        for i in range(a1, a2 + 1):
            for j in range(b1, b2 + 1):
                tmp += arr[i][j]
        if size == tmp: answer[1] += 1
        elif tmp == 0: answer[0] += 1
        else:
            amid = (a2 - a1) // 2
            bmid = (b2 - b1) // 2
            dvide_conqure(a1, a1 + amid, b1, b1 + bmid)
            dvide_conqure(a1 + amid + 1, a2, b1, b1 + bmid)
            dvide_conqure(a1, a1 + amid, b1 + bmid + 1, b2)
            dvide_conqure(a1 + amid + 1, a2, b1 + bmid + 1, b2)
    
    dvide_conqure(x1, x2, y1, y2)
    
    return answer
