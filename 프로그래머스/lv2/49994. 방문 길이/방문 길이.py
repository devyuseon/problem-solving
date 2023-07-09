def solution(dirs):    
    dx = {"U": -1, "D": 1, "R": 0, "L": 0}
    dy = {"U": 0, "D": 0, "R": 1, "L": -1}
    
    x, y = 0, 0 # 초기위치
    memo = set()
    answer = 0
    
    for d in dirs:
        nx, ny = x + dx[d], y + dy[d]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        tmp1 = f'{x}{nx}{y}{ny}' # x,y to nx,ny
        tmp2 = f'{nx}{x}{ny}{y}' # nx,ny to x,y
        if tmp1 not in memo and tmp2 not in memo:
            answer += 1
            memo.add(tmp1)

        x, y = nx, ny
    
    
    return answer