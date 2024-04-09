class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result, length = len(nums), len(nums)
        nums = sorted(set(nums))
        right = 0
        for left in range(len(nums)):
            # nums[left], nums[left] + length - 1
            while right < len(nums) and nums[right] < nums[left] + length:
                right += 1
            window = right - left
            result = min(result, length - window)
        return result