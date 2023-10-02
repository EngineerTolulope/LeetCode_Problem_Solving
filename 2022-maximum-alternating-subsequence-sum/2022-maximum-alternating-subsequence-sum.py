class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        cache = {}

        def depth_first_search(index, is_even):
            if index == len(nums):
                return 0
            if (index, is_even) in cache:
                return cache[(index, is_even)]

            num = nums[index] if is_even else -nums[index]
            result = max(num + depth_first_search(index + 1, not is_even),
                         depth_first_search(index + 1, is_even))
            cache[(index, is_even)] = result
            return result

        return depth_first_search(0, True)