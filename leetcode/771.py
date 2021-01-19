class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        J = jewels.split()
        for s in stones:
            if s in J:
                count += 1
        return count
