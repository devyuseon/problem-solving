def repeat_string(str,times):
    result = ""
    for s in str:
        tmp = [s]*times
        result += "".join(tmp)
    print(result)


N = int(input())
for _ in range(0, N):
    R, S = input().split()
    R = int(R)
    repeat_string(S,R)
