class Solution:
    import math
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)    # Intialize to ones
        
        # left to right
        prefix = 1
        for idx in range(len(nums)):
            output[idx] = prefix
            prefix *= nums[idx]
        
        # right to left
        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            output[idx] *= postfix 
            postfix *= nums[idx]
            
        
        return output

            
            
        