class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        def depth_first_search(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # decision to add nums[i]
            subset.append(nums[i])
            depth_first_search(i + 1)
            
            # decision to not add nums[i]
            subset.pop()
            depth_first_search(i + 1)
        
        
        depth_first_search(0)
        return result