class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)    # Most operations are O(1)
        longest = 0
        
        for num in nums_set:
            if (num - 1) not in nums_set:   # Check if it's a start of a sequence
                length = 0
                while (num + length) in nums_set:    # Continues until the end of the sequence
                    length += 1
                longest = max(longest, length)  # Takes the max of the two
                                
        return longest