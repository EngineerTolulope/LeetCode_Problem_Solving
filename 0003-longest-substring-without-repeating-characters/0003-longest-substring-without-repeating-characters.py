class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, result, charSet = 0, 0, set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            result = max(result, r - l + 1)
        return result