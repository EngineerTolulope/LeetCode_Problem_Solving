class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = []
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            self.prefix_sums.append(prefix_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sums[left - 1] if left > 0 else 0
        right_sum = self.prefix_sums[right]
        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)