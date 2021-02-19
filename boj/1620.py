import sys

dict = {}
reversed_dict = {}
N, M = map(int, input().split())

for i in range(1,N + 1):
    tmp = sys.stdin.readline().rstrip()
    dict[i] = tmp
    reversed_dict[tmp] = i

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    try:
        question = int(question)
    except ValueError:
        print(reversed_dict[question])
    else:
        print(dict[question])