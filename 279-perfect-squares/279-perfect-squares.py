class Solution:
    def numSquares(self, n: int) -> int:
        squares = [num**2 for num in range(0, n) if num**2 <= n]
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for target in range(1, n + 1):
            dp[target] = target
            for square in squares:
                if target - square < 0:
                    break
                if 1 + dp[target - square] < dp[target]:
                    dp[target] = 1 + dp[target - square]
        return dp[n]