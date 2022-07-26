class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Hash to store the count of each character 
        left = 0
        max_substring = 0
        
        for right in range(len(s)): # Left and Right pointers start at the same position
            count[s[right]] = 1 + count.get(s[right], 0)
            num_of_chars = right - left + 1 # This refers to how many characters we are at currently
            
            # Checks if number of different characters falls within the limit k
            if (num_of_chars - max(count.values())) <= k:
                max_substring = max(num_of_chars, max_substring)
            else:
                count[s[left]] -= 1 # We decrement the count and move the left pointer
                left += 1
        
        return max_substring
                
            
            
        