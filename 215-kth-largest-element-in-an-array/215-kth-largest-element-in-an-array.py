class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quick_select(left, right):
            pivot_num, pointer = nums[right], left
            
            for i in range(left, right):
                if nums[i] <= pivot_num:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[right] = nums[right], nums[pointer]
            
            if pointer < k:
                return quick_select(pointer + 1, right)
            elif pointer > k:
                return quick_select(left, pointer - 1)
            else:
                return nums[pointer]
        return quick_select(0, len(nums) - 1) 
        