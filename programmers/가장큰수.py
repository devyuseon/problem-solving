def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int(''.join(sorted(numbers, reverse=True, key = lambda x: x * 3))))