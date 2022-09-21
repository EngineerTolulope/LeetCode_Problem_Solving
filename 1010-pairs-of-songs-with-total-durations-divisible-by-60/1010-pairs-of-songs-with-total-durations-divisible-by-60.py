class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        count = [0] * 60
        result = 0
        for time in times:
            remainder = time % 60
            result += count[60 - remainder] if remainder > 0 else count[0]
            count[remainder] += 1
        return result