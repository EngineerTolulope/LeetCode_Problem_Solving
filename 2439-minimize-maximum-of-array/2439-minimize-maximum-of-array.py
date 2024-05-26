from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        result = 0

        for i in range(len(nums)):
            total += nums[i]
            result = max(result, (total + i) // (i + 1))
        
        return result
