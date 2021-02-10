import sys

words = []

N = int(input())
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

# 정렬
result = sorted(set(words), key=lambda x:(len(x),x))

# 출력
for s in result: print(s)