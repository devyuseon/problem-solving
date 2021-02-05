play = list(map(int, input().split()))
tmp = []

for i in range(1, 8):
    if play[i-1] < play[i]:
        tmp.append(1)
    else:
        tmp.append(-1)

if 1 in tmp and -1 in tmp:
    print('mixed')
elif 1 in tmp and -1 not in tmp:
    print('ascending')
elif -1 in tmp and 1 not in tmp:
    print('descending')