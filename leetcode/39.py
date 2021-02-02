from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, cur):
            result.append(cur)

            for i in range(index, len(nums)):
                dfs(i + 1, cur + [nums[i]])
        
        dfs(0, [])
        return result