class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        result = 0

        for num, count in num_count.items():
            if count == 1:
                return -1
            result += math.ceil(count / 3)
        return result