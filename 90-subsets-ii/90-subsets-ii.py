class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtracking(subset, i):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # we choose to include nums[i]
            subset.append(nums[i])
            backtracking(subset, i + 1)
            subset.pop()
            
            # we choose not to include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(subset, i + 1)
        backtracking([], 0)
        return result