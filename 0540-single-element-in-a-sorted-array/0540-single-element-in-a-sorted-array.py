class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if ((middle - 1 < 0 or nums[middle - 1] != nums[middle]) and
               (middle + 1 == len(nums) or nums[middle + 1] != nums[middle])):
               return nums[middle]
            
            left_size = middle - 1 if nums[middle - 1] == nums[middle] else middle
            if left_size % 2 == 1:
                right = middle - 1
            else:
                left = middle + 1