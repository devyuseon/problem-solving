def hanoi(n: int, from_pos, to_pos, sub_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    
    hanoi(n-1, from_pos, sub_pos, to_pos)
    print(from_pos, to_pos)
    hanoi(n-1, sub_pos, to_pos, from_pos)

N = int(input())

print(2**N - 1)
hanoi(N, 1, 3, 2)