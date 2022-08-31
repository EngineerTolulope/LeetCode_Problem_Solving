class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_here = nums[i] + nums[left] + nums[right]
                if abs(sum_here - target) < abs(result - target):
                    result = sum_here
                
                if sum_here < target:
                    left += 1
                else:
                    right -= 1
        return result
        