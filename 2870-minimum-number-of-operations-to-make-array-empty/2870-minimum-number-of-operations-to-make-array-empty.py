from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count the occurrences of each number in the list
        frequency = Counter(nums)
        operations = 0

        for count in frequency.values():
            if count == 1:
                return -1  # If any number appears only once, it's impossible to group
            
            # Calculate the minimum operations needed for this count
            # Prefer to group in triples, but use a pair if needed
            operations += (count // 3) + (1 if count % 3 != 0 else 0)
        
        return operations

# Example usage:
# solution = Solution()
# print(solution.minOperations([2, 3, 3, 3, 2, 4, 2, 4, 4, 4, 4]))  # Output: 4
# print(solution.minOperations([1, 2, 3]))  # Output: -1 (because each number appears only once)
