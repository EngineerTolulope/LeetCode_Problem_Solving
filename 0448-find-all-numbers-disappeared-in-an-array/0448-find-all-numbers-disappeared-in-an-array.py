class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -1 * abs(nums[index])
        
        current = 0
        for i, num in enumerate(nums):
            if num > 0:
                actual_num = i + 1
                nums[current] = actual_num
                current += 1
        return nums[:current]