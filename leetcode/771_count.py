import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        freq = collections.Counter(stones)
        for J in jewels:
            count += freq[J]
        return count
