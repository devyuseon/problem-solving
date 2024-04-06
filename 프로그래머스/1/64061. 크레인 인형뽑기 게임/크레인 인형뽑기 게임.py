from collections import deque

def solution(board, moves):
    answer = 0
    stack = []
    
    nboard = list(zip(*board))
    
    for i in range(len(board)):
        board[i] = list(nboard[i])
        board[i] = board[i][::-1]
        while True:
            if board[i][-1] == 0: board[i].pop()
            else: break
        
    for m in moves:
        m = m - 1
        if not board[m] or board[m][-1] == 0: # 맨 뒤에 있는 원소. 인형이 없으면 아무것도 하지 않음
            continue
        # 인형이 있다면 뽑는다.
        doll = board[m].pop()
        # stack의 맨 뒤와 같다면 터뜨림
        if stack:
            if stack[-1] == doll:
                answer += 2
                stack.pop()
                continue
        stack.append(doll)
    
    return answer
