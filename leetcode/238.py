from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        result = []

        # 왼쪽 곱셈
        tmp = 1
        for i in range(len(nums)):
            if i == 0:
                left.append(tmp)
            else:
                tmp *= nums[i-1]
                left.append(tmp)

        # 오른쪽 곱셈
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right.append(tmp)
            else:
                tmp *= nums[i+1]
                right.append(tmp)

        right = right[::-1]

        for i in range(len(left)):
            result.append(left[i] * right[i])

        return result
