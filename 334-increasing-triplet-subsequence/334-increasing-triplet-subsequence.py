class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        infinity = float('infinity')
        
        num_i, num_j = infinity, infinity
        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False