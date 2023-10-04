class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones_count, result = 0, 0
        for num in s:
            if num == "1":
                ones_count += 1
            else:
                result = min(1 + result, ones_count)

        return result