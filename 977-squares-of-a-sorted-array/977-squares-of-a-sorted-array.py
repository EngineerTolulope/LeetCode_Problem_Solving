class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1
        
        while left <= right:
            num_left, num_right = nums[left] ** 2, nums[right] ** 2
            
            if num_right > num_left:
                result.append(num_right)
                right -= 1
            else:
                result.append(num_left)
                left += 1
        result.reverse()
        return result
                
                
            