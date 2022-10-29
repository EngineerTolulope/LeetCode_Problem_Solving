class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def can_split(largest):
            subarray, current_sum = 1, 0
            for num in nums:
                current_sum += num
                if current_sum > largest:
                    subarray += 1
                    current_sum = num
                if subarray > m:
                    return False
            return subarray <= m
        
        
        left, right = max(nums), sum(nums)
        result = right
        while left <= right:
            middle = left + (right - left) // 2
            if can_split(middle):
                right = middle - 1
                result = middle
            else:
                left = middle + 1
        return result