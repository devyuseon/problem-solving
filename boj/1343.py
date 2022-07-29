# pypy3 113248kb / 112ms

def cover(cnt):
    global result
    
    if cnt % 2 != 0:
        result = '-1'
        return False
    
    for _ in range(cnt // 4):
        result += 'AAAA'
    cnt -= cnt // 4 * 4
    for _ in range(cnt // 2):
        result += 'BB'
    
    return True

board = input() + ' '
result = ''
cnt = 0

for i in range(len(board)):
    if board[i] == 'X':
        cnt += 1
    else:
        if cnt > 0:
            if not cover(cnt):
                break
            cnt = 0
        if board[i] != ' ':
            result += '.'

print(result.rstrip())