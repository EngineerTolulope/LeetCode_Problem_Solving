class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count, t_count = Counter(s), Counter(t)

        for char in t_count:
            if (char not in s_count) or (t_count[char] > s_count[char]):
                return char 