class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0

        while n > 1:
            result += n // 2
            n = math.ceil(n / 2)
        
        return result