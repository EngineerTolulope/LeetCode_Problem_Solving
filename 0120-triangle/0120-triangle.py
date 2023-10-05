class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, num in enumerate(row):
                dp[i] = min(dp[i] + num, dp[i + 1] + num)
        return dp[0]