class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0 : -1}
        total = 0

        for index, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder not in remainder_index:
                remainder_index[remainder] = index
            elif (index - remainder_index[remainder]) > 1:
                return True
        return False
            
