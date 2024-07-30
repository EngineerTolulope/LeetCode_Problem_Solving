from typing import Set

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Set of vowels for quick lookup
        vowels: Set[str] = {'a', 'e', 'i', 'o', 'u'}
        
        left, count, max_count = 0, 0, 0
        
        # Iterate over the string with the right pointer
        for right in range(len(s)):
            # Add to count if the current character is a vowel
            if s[right] in vowels:
                count += 1

            # Shrink the window if its size exceeds k
            while (right - left + 1) > k:
                if s[left] in vowels:
                    count -= 1
                left += 1

            # Update max_count if the current window size is exactly k
            if (right - left + 1) == k:
                max_count = max(max_count, count)
        
        return max_count

# Example usage:
# solution = Solution()
# print(solution.maxVowels("abciiidef", 3))  # Output: 3
# print(solution.maxVowels("aeiou", 2))  # Output: 2
# print(solution.maxVowels("leetcode", 3))  # Output: 2
