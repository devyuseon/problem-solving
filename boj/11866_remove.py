N, K = map(int, input().split())

li = [i for i in range(1, N + 1)]
result = []
cur =  0

for _ in range(N):
    result.append(li[(cur + K - 1) % len(li)])
    del li[(cur + K - 1) % len(li)]
    cur += K - 1

            
print("<", end="")
for i, n in enumerate(result):
    if i == len(result) - 1:
        print(n, end="")
    else:
        print(n, end=", ")
print(">")