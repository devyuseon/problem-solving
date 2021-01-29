from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev = []
        answer = []
        def dfs(elements: List[int]):
            if len(elements) == 0:
                answer.append(prev[:])

            for e in elements:
                next = elements[:]
                prev.append(e)
                next.remove(e)
                dfs(next)
                prev.pop()

        dfs(nums)
        return answer