class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        default_value = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = default_value
        
        for i in range(len(nums)):
            value = abs(nums[i])
            if value in range(1, len(nums) + 1):
                if nums[value - 1] > 0:
                    nums[value - 1] *= -1

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                return i
        return len(nums) + 1
        
        
                