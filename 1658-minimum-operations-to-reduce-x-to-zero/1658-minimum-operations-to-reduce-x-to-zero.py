class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0

        result, current_sum = sys.maxsize, 0
        for right in range(len(nums)):
            current_sum += nums[right]

            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                result = min(result, len(nums) - (right - left + 1))
        return result if result != sys.maxsize else -1