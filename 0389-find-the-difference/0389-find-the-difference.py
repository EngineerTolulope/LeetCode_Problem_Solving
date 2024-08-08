from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Count the characters in both strings
        s_count = Counter(s)
        t_count = Counter(t)

        # Find the character that differs
        for char in t_count:
            if t_count[char] > s_count[char]:
                return char
