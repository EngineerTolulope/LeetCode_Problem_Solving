class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('infinity')
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_here = nums[i] + nums[left] + nums[right]
                if sum_here == target:
                    return sum_here
                
                if abs(sum_here - target) < abs(result - target):
                    result = sum_here
                
                if sum_here <= target:
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                else:
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return result
        