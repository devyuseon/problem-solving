from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def dfs(sum, index, cur):
            if sum < 0:
                return
            if sum == 0:
                answer.append(cur)
                return

            for i in range(index, len(candidates)):
                dfs(sum - candidates[i], i, cur + [candidates[i]])

        dfs(target, 0, [])
        return answer



