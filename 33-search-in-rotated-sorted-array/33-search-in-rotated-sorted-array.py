class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            
            if nums[middle] == target:
                return middle
            
            # For checking the left part
            if nums[start] <= nums[middle]:
                if nums[start] <= target <= nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            
            # For checking the right part
            else:
                if nums[middle] <= target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        
        return -1
            