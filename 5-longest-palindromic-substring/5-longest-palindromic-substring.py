class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s)):
            # odd length palindromes
            left, right = i, i        
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_string = s[left:right+1]
                if len(current_string) > len(longest):
                    longest = current_string
                left -= 1
                right += 1
                
            # even length palindromes
            left, right = i, i + 1        
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_string = s[left:right+1]
                if len(current_string) > len(longest):
                    longest = current_string
                left -= 1
                right += 1
        return longest