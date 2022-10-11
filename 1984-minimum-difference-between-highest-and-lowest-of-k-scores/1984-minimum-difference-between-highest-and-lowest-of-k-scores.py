class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, result = 0, sys.maxsize
        for right in range(k - 1, len(nums)):
            result = min(result, nums[right] - nums[left])
            left += 1
        return result