class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        current_min, current_max = 1, 1
        
        for num in nums:
            temp_variable = current_max * num
            current_max = max(temp_variable, num, current_min * num)
            current_min = min(temp_variable, num, current_min * num)
            result = max(result, current_max)
        
        return result