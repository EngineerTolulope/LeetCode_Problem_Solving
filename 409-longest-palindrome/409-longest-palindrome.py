class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = {}
        for char in s:
            char_counts[char] = 1 + char_counts.get(char, 0)
            
        result, found_odd = 0, False
        for char, count in char_counts.items():
            if count % 2 == 0:
                result += count
            else:
                found_odd = True
                result += count - 1
        
        return result + 1 if found_odd else result
        