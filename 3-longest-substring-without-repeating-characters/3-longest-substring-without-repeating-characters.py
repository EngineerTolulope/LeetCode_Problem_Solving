class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()   # Set to store the characters
        
        left = 0
        max_substring = 0
        
        for right in range(len(s)): # Right and Left pointers start at the same point
            while s[right] in chars_set:
                chars_set.remove(s[left])
                left += 1
                
            chars_set.add(s[right])
            max_substring = max(max_substring, len(s[left:right+1]))

        return max_substring
                
            