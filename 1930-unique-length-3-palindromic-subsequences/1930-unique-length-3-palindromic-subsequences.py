class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result, left_chars, right_chars = set(), set(), {}
        for char in s:
            right_chars[char] = 1 + right_chars.get(char, 0)
            
        for middle in s:
            right_chars[middle] -= 1
            if right_chars[middle] == 0:
                right_chars.pop(middle)
            
            for outer in left_chars:
                if outer in right_chars:
                    result.add((middle, outer))
            
            left_chars.add(middle)
        return len(result)
