class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        # 소문자로 변환
        for i in s:
            if i.isalnum():
                strs.append(i.lower())

        tmp = strs

        # 펠린드롭 판단
        while len(tmp) > 1:
            if strs.pop(0) != tmp.pop():
                return False
        return True
