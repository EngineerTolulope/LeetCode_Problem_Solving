class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_count, result = 0, 0
        
        for num in nums:
            if current_count == 0:
                result = num
            current_count += 1 if result == num else -1
        return result
                