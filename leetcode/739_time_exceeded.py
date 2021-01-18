class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        start = 0
        end = 1
        result = []
        last = len(T) - 1

        while start != last:
            if T[start] < T[end]:
                result.append(end - start)
                start += 1
                end = start + 1
                continue
            else:
                if end == last:
                    result.append(0)
                    start += 1
                    end = start + 1
                else:
                    end += 1
        result.append(0)

        return result
