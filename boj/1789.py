S = int(input())
SUM = 0
N = 1

while True:
    SUM += N
    if SUM > S:
        break
    else:
        N += 1
        
if SUM == S:
    print(N)
else:
    print(N - 1)

# 128ms
# S = int(input())

# N = 1
# while N * (N + 1) < 2 * S and N * (N + 1) != 2 * S:
#     N += 1

# if N * (N + 1) == 2 * S:
#     print(N)
# else:
#     print(N - 1)

# 132ms
# S = int(input())
# N = 1
# while N * (N + 1)/2 <= S:
#     N += 1
# print(N - 1)