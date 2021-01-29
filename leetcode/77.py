from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        prev = []
        answer= []

        def dfs(k, next):
            if len(prev) == k:
                answer.append(prev[:]) # 참조 전달하지 않도록
            
            for i in range(0, len(next)):
                prev.append(next[0])
                next = next[1, len(next)]
                dfs(k, next[:])
                prev.pop()

        return answer
