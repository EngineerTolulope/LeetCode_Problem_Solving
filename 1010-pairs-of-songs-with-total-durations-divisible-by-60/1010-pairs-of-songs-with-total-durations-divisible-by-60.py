class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        count = [0] * 60
        result = 0
        for time in times:
            result += count[-time % 60]
            count[time % 60] += 1
        return result