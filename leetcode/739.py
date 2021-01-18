class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0]*len(T)
        for i, n in enumerate(T):
            while stack and n > T[stack[-1]]:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)
        return result
