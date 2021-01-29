from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        answer = []

        def dfs(tmp, start, k):
            if k == 0:
                answer.append(tmp[:])
            
            for i in range(start, n + 1):
                tmp.append(i)
                dfs(tmp, i + 1, k - 1)
                tmp.pop()
        
        dfs([], 1, k)

        return answer
