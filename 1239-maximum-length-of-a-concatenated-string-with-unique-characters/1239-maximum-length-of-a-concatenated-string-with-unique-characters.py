from typing import List
from collections import Counter

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Set to store unique characters from the current combination
        unique_chars = set()

        def hasDuplicates(existing_chars: set, new_string: str) -> bool:
            """
            Check if adding characters from new_string to existing_chars results in duplicates.
            """
            combined_counter = Counter(existing_chars) + Counter(new_string)
            return any(count > 1 for count in combined_counter.values())

        def backtrack(index: int) -> int:
            """
            Use backtracking to explore all possible combinations.
            """
            # Base case: if we've considered all strings in arr
            if index == len(arr):
                return len(unique_chars)

            # Option 1: Exclude the current string and proceed
            max_length = backtrack(index + 1)

            # Option 2: Include the current string if it doesn't introduce duplicates
            if not hasDuplicates(unique_chars, arr[index]):
                # Add current string's characters to the unique set
                unique_chars.update(arr[index])
                # Recursively calculate the max length by including this string
                max_length = max(max_length, backtrack(index + 1))
                # Backtrack: remove current string's characters after processing
                unique_chars.difference_update(arr[index])

            return max_length

        # Start backtracking from the first index
        return backtrack(0)
