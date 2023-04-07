s = input()
i = 0

while i < len(s):
    if i + 10 < len(s):
        print(s[i:i + 10])
        i += 10
    else:
        print(s[i:])
        break