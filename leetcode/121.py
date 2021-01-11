from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) > 1:
            # 계속 상승하는 그래프일 경우를 위해 0 넣고 시작
            low_point_index = [0]
            profits = []

            # 저점 인덱스 저장
            for i in range(1, len(prices) - 1):
                if (prices[i-1] > prices[i]):
                    low_point_index.append(i)

            # profit 구하기
            for n in low_point_index:
                tmp = max(prices[n+1:]) - prices[n]
                if tmp > 0:
                    profits.append(tmp)

            if len(profits) > 0:
                return max(profits)
            else:
                return 0

        # len(prices)가 0,1인 경우 profit 0
        else:
            return 0


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
