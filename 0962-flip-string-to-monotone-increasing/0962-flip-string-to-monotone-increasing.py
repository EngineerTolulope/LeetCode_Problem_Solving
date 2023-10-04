class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones_count, flips = 0, 0
        for num in s:
            if num == "1":
                ones_count += 1
            else:
                flips = min(flips + 1, ones_count)

        return flips