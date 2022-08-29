# pypy3 117128kb / 120ms

brac = input()
stack = []
res = 0
for i in range(len(brac)):
    if brac[i] == '(': 
        stack.append('(')
    else: 
        if brac[i - 1] == '(': # i=0일때 ) 못옴. 레이저
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
print(res)