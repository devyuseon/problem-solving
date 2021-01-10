import collections
from typing import OrderedDict
from typing import List

"""
<브루트 포스 - 타임아웃>
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profits.append(prices[j] - prices[i])
        if len(profits) == 0:
            return 0
        else:
            return max(profits)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = {}
        for i, n in enumerate(prices):
            stock[i] = n

        # 오름차순으로 정렬 , key기준
        OrderedDict(stock.sort(stock.items(), lambda x: x[0]))

        for i in range(len(prices), 0, -1):
