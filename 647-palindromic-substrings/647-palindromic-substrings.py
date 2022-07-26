class Solution:
    def count_palindromes(self, s, left, right):
        count = 0
        
        # While we are in bounds of s and the characters at the left and right are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1   # Moves pointer to the left character
            right += 1  # Moves pointer to the right character
        
        return count
            
    
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Counts odd palidromes, left and right at same place
            count += self.count_palindromes(s, i, i)
            
            # Counts even palindromes, left and right next to each other
            count += self.count_palindromes(s, i, i+1)
            
        return count