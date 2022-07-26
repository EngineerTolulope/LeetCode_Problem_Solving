class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            left, right = idx + 1, len(nums) - 1
            
            while left < right:
                current_sum = num + nums[left] + nums[right]
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1   # We need to keep moving one of the pointers to find other solutions
                    
                    # If the same number is repeated we have to keep appending our left pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
        return result
            

        
            
        
        