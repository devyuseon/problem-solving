from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        sum = 0
        for i in range(1, len(nums), 2):
            sum += nums[i]
        return sum
