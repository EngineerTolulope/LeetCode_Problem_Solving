class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_rob = max(self.house_robber_1(nums[1:]), 
                      self.house_robber_1(nums[:-1]))
        return max_rob
        
        
    def house_robber_1(self, nums):
        rob_1, rob_2 = 0, 0
        
        for num in nums:
            new_rob = max(rob_1 + num, rob_2)
            rob_1 = rob_2
            rob_2 = new_rob
        return rob_2