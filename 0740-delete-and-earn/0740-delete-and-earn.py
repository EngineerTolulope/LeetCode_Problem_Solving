class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        nums = sorted(list(set(nums)))
        earn_1, earn_2 = 0, 0
        for i, num in enumerate(nums):
            current_earn = num_count[num] * num
            if i > 0 and num - 1 == nums[i - 1]:
                temp = earn_2
                earn_2 = max(current_earn + earn_1, earn_2)
                earn_1 = temp
            else:
                temp = earn_2
                earn_2 = current_earn + earn_2
                earn_1 = temp
        return earn_2