class Solution:
    def minFlips(self, s: str) -> int:
        # Length of the original string
        n = len(s)
        
        # Double the string to handle rotations
        s = s + s
        
        # Generate alternating strings
        alt1 = ''.join('1' if i % 2 else '0' for i in range(len(s)))
        alt2 = ''.join('0' if i % 2 else '1' for i in range(len(s)))
        
        min_flips = n  # Initialize result with maximum possible value
        left = 0  # Left pointer for the sliding window
        diff1 = diff2 = 0  # Counters for differences with alt1 and alt2
        
        for right in range(len(s)):
            # Count mismatches for current right position
            if alt1[right] != s[right]:
                diff1 += 1
            if alt2[right] != s[right]:
                diff2 += 1
            
            # Adjust window size if it exceeds the original string length
            if (right - left + 1) > n:
                if alt1[left] != s[left]:
                    diff1 -= 1
                if alt2[left] != s[left]:
                    diff2 -= 1
                left += 1
            
            # Update result if the window size is equal to the original string length
            if (right - left + 1) == n:
                min_flips = min(min_flips, diff1, diff2)
        
        return min_flips

# Example usage:
# solution = Solution()
# print(solution.minFlips("111000"))  # Output: 2
# print(solution.minFlips("01001001101"))  # Output: 2
