def longestPalindrome(self, s: str) -> str:
    if len(s) < 2 or s[:] == s[::-1]:
        return s

    palindrome = []
    length = len(s)
    start = 0
    end = 0

    while(start != length-1):
        if end == length:
            start += 1
            end = start
        tmp = s[start:end+1]
        if tmp[:] == tmp[::-1]:
            palindrome.append(tmp)
        end += 1

    if len(palindrome) == 0:
        return s[0]
    else:
        return sorted(palindrome, key=len).pop()

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            tmp = s[i:j+1]
            if tmp == tmp[::-1]:
                palindrome.append(tmp)
    if len(palindrome) == 0:
        return s[0]
    else:
        return sorted(palindrome, key=len).pop()
