class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index, is_even):
            if index == len(nums):
                return 0
            if (index, is_even) in cache:
                return cache[(index, is_even)]

            num = nums[index] if is_even else -1 * nums[index] 
            result = max(num + dfs(index + 1, not is_even), dfs(index + 1, is_even))
            cache[(index, is_even)] = result
            return result
        return dfs(0, True)
