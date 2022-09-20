class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if ((middle == 0 or nums[middle] > nums[middle - 1]) and
                (middle == len(nums) - 1 or nums[middle] > nums[middle + 1])):
                return middle
            elif middle > 0 and nums[middle - 1] > nums[middle]:
                right = middle - 1
            elif middle < len(nums) - 1 and nums[middle + 1] > nums[middle]:
                left = middle + 1