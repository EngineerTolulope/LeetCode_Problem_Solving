class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        previous_total = {0 : 1}   # dynamic programming
        for total in range(1, target + 1):
            previous_total[total] = 0
            for num in nums:
                previous_total[total] += previous_total.get(total - num, 0)
        return previous_total[target]