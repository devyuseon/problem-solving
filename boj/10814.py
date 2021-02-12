import sys

member = []
N = int(input())
for i in range(N):
    tmp = sys.stdin.readline().split()
    tmp.append(i)
    member.append(tmp)

member.sort(key=lambda x: (int(x[0]),x[2]))
for m in member:
    print(m[0], m[1])