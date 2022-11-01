class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        visited = [False] * len(nums)
        
        
        def backtrack(i, remain_subsets, subset_sum):
            if remain_subsets == 0:
                return True
            if subset_sum == target:
                return backtrack(0, remain_subsets - 1, 0)
            
            for j in range(i, len(nums)):
                if ((j > 0 and not visited[j - 1] and nums[j] == nums[j - 1]) or
                    (visited[j] or subset_sum + nums[j] > target)):
                    continue
                visited[j] = True
                if backtrack(j + 1, remain_subsets, subset_sum + nums[j]):
                    return True
                visited[j] = False
            return False
        
        
        return backtrack(0, k, 0)