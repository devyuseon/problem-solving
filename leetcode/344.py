def reverseString(self, s: List[str]) -> None:
    i = len(s) // 2

    while i > 0:
        s[i-1], s[len(s)-i] = s[len(s)-i], s[i-1]
        i -= 1
