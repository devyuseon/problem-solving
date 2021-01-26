import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        count = collections.Counter(nums)

        for tuple in count.most_common(k):
            answer.append(tuple[0])

        return answer