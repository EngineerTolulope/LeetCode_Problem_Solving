class Solution:
    def __init__(self):
        self.permutations = []
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.permutations
    
    
    def backtrack(self, nums, path):
        if not nums:
            return self.permutations.append(path)
        
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
                
        