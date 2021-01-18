import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = collections.Counter(s)
