class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0 : 1}
        result, current_sum = 0, 0
        
        for num in nums:
            current_sum += num
            difference = current_sum - k
            
            result += prefix_sums.get(difference, 0)
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
        return result
            
            
            