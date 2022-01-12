for _ in range(int(input())):
    A, B = map(lambda x: int(x, 2), input().split())
    print(bin(A + B)[2:]) 