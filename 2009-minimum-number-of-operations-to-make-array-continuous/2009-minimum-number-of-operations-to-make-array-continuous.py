class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        result = len(nums)
        right = 0

        for left in range(len(nums)):
            while right < len(nums) and nums[right] < nums[left] + result:
                right += 1
            
            window = right - left
            result = min(result, len(nums) - window)
        
        return result