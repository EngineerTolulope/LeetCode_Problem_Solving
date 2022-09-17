class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        left = 0
        for right in range(len(needle) - 1, len(haystack)):
            if haystack[left:right+1] == needle:
                return left
            left += 1
        return -1