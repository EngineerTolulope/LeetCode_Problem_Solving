class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0
        
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if length > 0 and char == ' ':
                break
            if char.isalpha():
                length += 1
        return length
        
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length