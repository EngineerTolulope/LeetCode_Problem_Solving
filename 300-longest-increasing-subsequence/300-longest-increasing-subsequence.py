class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    longest[i] = max(longest[i], 1 + longest[j])
        return max(longest)