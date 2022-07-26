class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            mid_num = nums[middle]
            if mid_num < target:
                left = middle + 1
            elif mid_num > target:
                right = middle - 1
            else:
                return middle
        return left