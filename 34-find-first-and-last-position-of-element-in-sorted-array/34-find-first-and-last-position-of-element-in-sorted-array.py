class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(left_biased):
            left, right, i = 0, len(nums) - 1, -1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    i = middle
                    if left_biased:
                        right = middle - 1
                    else:
                        left = middle + 1
            return i
        
        
        left_bound = binary_search(True)
        right_bound = binary_search(False)
        return [left_bound, right_bound]