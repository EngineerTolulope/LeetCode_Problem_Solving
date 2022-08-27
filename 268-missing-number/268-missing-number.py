class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(nums):
            result ^= num ^ i
        result ^= i + 1
        return result