class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {}
        total = 0

        for index, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder == 0 and index >= 1:
                return True

            if remainder in remainder_index:
                if index - remainder_index[remainder] > 1:
                    return True
            else:
                remainder_index[remainder] = index

        return False

    def checkSubarraySum_(self, nums: List[int], k: int) -> bool:
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
            
