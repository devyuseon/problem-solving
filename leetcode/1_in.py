class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        # 몇번째 원소인지 알려주는 enumerate()
        for i, n in enumerate(nums):
            tmp = target - n
            if tmp in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(tmp) + (i + 1)
