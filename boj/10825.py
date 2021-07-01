# 리스트, 588ms
import sys

N = int(input())

grade = []

for _ in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    grade.append([name, int(kor), int(eng), int(math)])

grade.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for result in grade:
    print(result[0])

# 딕셔너리, 580ms
"""
import sys

N = int(input())

grade = dict()

for _ in range(N):
    name, kr, en, mt = sys.stdin.readline().split()
    kr, en, mt = map(int, [kr, en, mt])
    grade[name] = [kr, en, mt]

for x in sorted(grade.items(),\
     key = lambda x : (-x[1][0], x[1][1], -x[1][2], x[0])):
    print(x[0])
"""

# 딕셔너리, 640ms
"""
import sys

N = int(input())

grade = dict()

for _ in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    grade[name] = [int(kor), int(eng), int(math)]

for x in sorted(grade.items(),\
     key = lambda x : (-x[1][0], x[1][1], -x[1][2], x[0])):
    print(x[0])
"""