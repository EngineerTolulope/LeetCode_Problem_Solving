from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array to enable incrementally building the result
        arr.sort()

        # Start with the first element as 1
        max_element = 0
        
        # Traverse the sorted array
        for num in arr:
            # Increment the previous element by 1 or take the current value if it's smaller
            max_element = min(max_element + 1, num)
        
        # The maximum possible element after decrementing and rearranging
        return max_element

# Example usage:
# solution = Solution()
# print(solution.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))  # Output: 2
