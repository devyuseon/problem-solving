class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        tmp = []
        for i, n in enumerate(s):
            if n not in tmp:
                tmp.append(n)
            else:
                substr.append(''.join(tmp))
                tmp = []
                i -= 1
        max_len = sorted(substr, key=lambda x: len(x), reverse=True)
        return len(max_len[0])
