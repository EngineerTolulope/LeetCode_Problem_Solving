class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulo = 10 ** 9 + 7
        nums.sort()
        result = 0
        
        right = len(nums) - 1
        for left in range(len(nums)):
            while (nums[left] + nums[right]) > target and left <= right:
                right -= 1
            
            if left <= right:
                result += 1 << (right - left)  # (2 ** (right - left))
                result %= modulo
        return result