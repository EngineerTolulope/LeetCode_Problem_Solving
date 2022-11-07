class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        new_nums = self.nums.copy()
        nums_len = len(new_nums)
        for i in range(nums_len):
            j = randint(i, nums_len - 1)
            new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
        return new_nums
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()