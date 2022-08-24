class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, max_length = 0, 0
        previous_count = {}
        previous_count[0] = -1
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in previous_count:
                max_length = max(max_length, i - previous_count[count])
            else:
                previous_count[count] = i
        return max_length