class Solution:
    def minFlips(self, s: str) -> int:
        window_length = len(s)
        s = s + s
        alt1, alt2 = "", ""

        for i in range(len(s)):
            alt1 += "1" if i % 2 else "0"
            alt2 += "0" if i % 2 else "1"

        result = len(s)
        left, diff1, diff2 = 0, 0, 0
        for right in range(len(s)):
            if alt1[right] != s[right]:
                diff1 += 1
            if alt2[right] != s[right]:
                diff2 += 1
            
            if (right - left + 1) > window_length:
                if alt1[left] != s[left]:
                    diff1 -= 1
                if alt2[left] != s[left]:
                    diff2 -= 1
                left += 1
            
            if (right - left + 1) == window_length:
                result = min(result, diff1, diff2)
            
        return result

