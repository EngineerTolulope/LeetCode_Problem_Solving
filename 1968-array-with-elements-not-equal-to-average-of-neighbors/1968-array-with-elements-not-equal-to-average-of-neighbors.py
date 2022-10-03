class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0] * len(nums)
        
        i, j = 0, 0
        while i < len(nums):
            result[i] = nums[j]
            j += 1
            i += 2
        
        i = 1
        while i < len(nums):
            result[i] = nums[j]
            j += 1
            i += 2
        return result