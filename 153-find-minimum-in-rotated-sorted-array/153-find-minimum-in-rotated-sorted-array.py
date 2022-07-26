class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1  # Left and right pointers
        min_num = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:    # This is true if the array has been rotated len(nums) times
                 min_num = min(nums[left], min_num)
            
            middle = (left + right) // 2
            min_num = min(min_num, nums[middle])
            
            if nums[left] <= nums[middle]:  # If true then we move to the right, since left has been checked
                left = middle + 1
            else:
                right = middle - 1
        return min_num