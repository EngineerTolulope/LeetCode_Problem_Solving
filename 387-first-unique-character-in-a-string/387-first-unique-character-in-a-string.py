class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            count = char_count.get(char, 0)
            if count >= 2:
                continue
            char_count[char] = count + 1
        
        for i in range(len(s)):
            char = s[i]
            if char_count[char] == 1:
                return i
        return -1