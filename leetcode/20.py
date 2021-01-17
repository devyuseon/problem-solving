class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in bracket:
                stack.append(char)  # opened bracket
            elif not stack or bracket[char] != stack.pop():
                return False

        return len(stack) == 0
