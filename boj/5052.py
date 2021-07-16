import sys

def is_consist(phones: list):
    for i in range(0, len(phones) - 1):
        if phones[i] == phones[i + 1][0 : len(phones[i])]:
            return False
    return True

t = int(input()) # 테스트케이스 수

for _ in range(t):
    n = int(input()) # 전화번호 수
    phones = [] # 전화번호 목록
    for _ in range(n): phones.append(sys.stdin.readline().strip())
    phones.sort()

    if is_consist(phones) == True:
        print("YES")
    else:
        print("NO")