N, M = map(int, input().split())
A: list = list(map(int, input().split()))
B: list = list(map(int, input().split()))

n = 0
m = 0

while n <= N - 1 and m <= M - 1:
    if A[n] < B[m]:
        print(A[n], end=" ")
        n += 1
    elif A[n] == B[m]:
        print(A[n], end=" ")
        print(B[m], end=" ")
        n += 1
        m += 1
    else:
        print(B[m], end=" ")
        m += 1

# A쪽이 남음
if m + 1 > M:
    for i in range(n, N):
        print(A[i], end=" ")

# B쪽이 남음
if n + 1 > N:
    for i in range(m, M):
         print(B[i], end=" ")

"""
N, M = map(int, input().split())
A: list = list(map(int, input().split()))
B: list = list(map(int, input().split()))

result = [0 for _ in range(N + M)]
n = 0
m = 0
index = 0

while n <= N - 1 and m <= M - 1:
    if A[n] <= B[m]:
        result[index] = A[n]
        n += 1
    else:
        result[index] = B[m]
        m += 1
    index += 1

# A쪽이 남음
if m + 1 > M:
    for i in range(n, N):
        result[index] = A[i]
        index += 1

# B쪽이 남음
if n + 1 > N:
    for i in range(m, M):
        result[index] = B[i]
        index += 1
    
for x in result: print(x, end=" ")
"""