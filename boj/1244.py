import sys
input = sys.stdin.readline

n = int(input())  # 스위치 수
switch = [-1] + list(map(int, input().split()))
m = int(input())  # 학생 수
stu = [tuple(map(int, input().split())) for _ in range(m)]  # 학생 스위치 정보


def male(k):
    for i in range(k, n + 1, k):
        switch[i] = 1 - switch[i]


def female(k):
    switch[k] = 1 - switch[k]
    for i in range(n // 2):
        if k + i > n or k - i < 1: break
        if switch[k + i] == switch[k - i]:
            switch[k + i] = 1 - switch[k + i]
            switch[k - i] = 1 - switch[k - i]
        else:
            break


for sex, s in stu:
    if sex == 1:
        male(s)
    else:
        female(s)

for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()