class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        t_chars, window = {}, {}  # The character counts
        for char in t:
            t_chars[char] = 1 + t_chars.get(char, 0)
            
        have, need = 0, len(t_chars)    # Variables to help us check if we satisfy the condition
        result, result_length = [0, 0], float("infinity") # The results index and length
        
        left = 0
        for right in range(len(s)): # Left and Right pointers start at the same point
            char = s[right]
            window[char] = 1 + window.get(char, 0)  # Increments the character in our window count
            
            # If the character is in t and the count are equal
            if char in t_chars and window[char] == t_chars[char]:
                have += 1
            
            while have == need:
                length = (right - left + 1)
                
                if length <= result_length: # update our result if the length is smaller
                    result = [left, right]  # Stores the new indices
                    result_length = length
                    
                # Pop elements from the left of our window
                window[s[left]] -= 1 # decrements our window count
                if s[left] in t_chars and window[s[left]] < t_chars[s[left]]:
                    have -= 1   # Decrements our have only when we no longer satisfy the needed condition
                
                left += 1   # moves to the next character
        
        left, right = result  
        return s[left:right+1] if result_length != float("infinity") else ""
        
        