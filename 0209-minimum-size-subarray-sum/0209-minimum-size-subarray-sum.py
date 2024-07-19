class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total, result = 0, 0, sys.maxsize

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        
        return result if result != sys.maxsize else 0