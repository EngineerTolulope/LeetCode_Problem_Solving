class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_idx:
                return [num_idx[diff], i]
            
            num_idx[num] = i