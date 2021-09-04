from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for xi, x in enumerate(nums):
            y = target - x
            if y in nums:
                yi = nums.index(y)
                if yi == xi:
                    if y in nums[xi+1:]:
                        yi = nums.index(y, xi+1)
                    else:
                        continue
                return [xi, yi]
